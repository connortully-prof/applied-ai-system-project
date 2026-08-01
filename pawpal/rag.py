from __future__ import annotations

import logging
import re
from dataclasses import dataclass
from pathlib import Path

LOGGER = logging.getLogger("pawpal")
if not LOGGER.handlers:
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
    LOGGER.addHandler(handler)
LOGGER.setLevel(logging.INFO)
LOGGER.propagate = False


@dataclass(frozen=True)
class KnowledgeEntry:
    title: str
    content: str
    keywords: tuple[str, ...]


class PawPalRAGSystem:
    """A lightweight retrieval-augmented pet care assistant."""

    def __init__(self, knowledge_path: str | Path | None = None, knowledge_sources: list[str | Path] | None = None) -> None:
        default_path = Path(__file__).resolve().parents[1] / "data" / "pet_care_knowledge.txt"
        sources = list(knowledge_sources) if knowledge_sources else []
        if knowledge_path is not None:
            sources.insert(0, knowledge_path)
        if not sources:
            sources = [default_path]

        self.knowledge_paths = [Path(source) for source in sources]
        self.knowledge_base = self._load_knowledge_base()

    def _load_knowledge_base(self) -> list[KnowledgeEntry]:
        chunks = []
        for path in self.knowledge_paths:
            if not path.exists():
                LOGGER.warning("Knowledge base not found at %s", path)
                continue

            raw_text = path.read_text(encoding="utf-8")
            for block in raw_text.split("\n\n"):
                block = block.strip()
                if not block:
                    continue
                lines = [line.strip() for line in block.splitlines() if line.strip()]
                if not lines:
                    continue
                title = lines[0]
                body = " ".join(lines[1:]) if len(lines) > 1 else ""
                keywords = tuple(sorted(set(re.findall(r"[a-zA-Z]+", (title + " " + body).lower()))))
                chunks.append(KnowledgeEntry(title=title, content=body, keywords=keywords))

        LOGGER.info("Loaded %s knowledge entries", len(chunks))
        return chunks

    def _tokenize(self, text: str) -> set[str]:
        return set(re.findall(r"[a-zA-Z]+", text.lower()))

    def _retrieve(self, query: str, limit: int = 2) -> list[KnowledgeEntry]:
        if not self.knowledge_base:
            return []

        query_tokens = self._tokenize(query)
        scored = []

        for entry in self.knowledge_base:
            overlap = len(query_tokens & set(entry.keywords))
            title_bonus = 2 if any(token in entry.title.lower() for token in query_tokens) else 0
            score = overlap + title_bonus
            if score > 0:
                scored.append((score, entry))

        scored.sort(key=lambda item: item[0], reverse=True)
        return [entry for _, entry in scored[:limit]]

    def _confidence_score(self, retrieved: list[KnowledgeEntry], query: str) -> float:
        if not retrieved:
            return 0.25

        query_tokens = self._tokenize(query)
        score = 0.0
        for entry in retrieved:
            overlap = len(query_tokens & set(entry.keywords))
            score += overlap / max(1, len(query_tokens))

        normalized = min(1.0, score / max(1, len(retrieved)))
        return round(max(0.25, min(0.98, 0.55 + normalized * 0.43)), 2)

    def answer(self, user_query: str) -> str:
        if not user_query or not user_query.strip():
            LOGGER.warning("Empty user query received")
            return "Please provide a question about your pet’s health or care needs."

        query = user_query.strip()
        query_lower = query.lower()
        pet_related_terms = {
            "pet", "dog", "cat", "puppy", "kitten", "animal", "vet", "veterinary",
            "health", "illness", "symptom", "fever", "diet", "care", "behavior"
        }

        if not any(term in query_lower for term in pet_related_terms):
            LOGGER.warning("Guardrail triggered for non-pet query: %s", query)
            return "This assistant is designed for pet care guidance only. Please ask about a dog, cat, or other pet health issue."

        try:
            relevant_entries = self._retrieve(query)
            if not relevant_entries:
                relevant_entries = self.knowledge_base[:2]

            context = " ".join(f"{entry.title}: {entry.content}" for entry in relevant_entries)
            confidence = self._confidence_score(relevant_entries, query)

            emergency_signals = [
                "fever", "weak", "not eating", "breathing", "collapse", "vomiting",
                "diarrhea", "seizure", "bleeding", "limping", "labored", "couldn't wake"
            ]
            is_emergency = any(signal in query_lower for signal in emergency_signals)

            if is_emergency:
                response = (
                    "Based on the retrieved pet care guidance, this situation needs prompt veterinary attention. "
                    "If your pet has a fever, weakness, breathing trouble, collapse, or severe symptoms, contact an emergency vet immediately. "
                    "Keep your pet calm, stop exercise, and avoid giving human medication without veterinary advice."
                )
            else:
                response = (
                    "Based on the retrieved pet care guidance, start with the safest next steps: "
                    "monitor symptoms closely, maintain hydration, avoid sudden diet changes, and contact a vet if the issue persists or worsens."
                )

            answer_text = (
                f"{response}\n\nRelevant guidance: {context}\n\n"
                f"Confidence: {confidence:.2f}\n\n"
                "If symptoms continue, worsen, or your pet seems unstable, schedule a veterinary exam promptly."
            )
            LOGGER.info("Generated answer for query: %s | confidence=%.2f", query, confidence)
            return answer_text
        except Exception:  # pragma: no cover - safety net for runtime issues
            LOGGER.exception("Failed to answer user query")
            return "I could not safely answer that request. Please rephrase the question and include your pet's symptoms or concern."


if __name__ == "__main__":
    system = PawPalRAGSystem()
    sample = "My dog has a fever and seems weak. What should I do?"
    print(system.answer(sample))

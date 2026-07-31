# PawPal AI Pet Care Assistant

## Original Project Context

This project is the evolved version of my original Module 1–3 PawPal project. In that earlier work, I built a pet-care assistant concept focused on helping owners understand common symptoms, wellness patterns, and safe next steps for their animals. The original goal was to combine basic AI support with practical pet health guidance in a way that felt useful, accessible, and cautious rather than overly confident.

## Title and Summary

PawPal is a lightweight AI-powered pet care assistant designed to help owners ask practical questions about pet symptoms, wellness, diet, and treatment caution. It matters because pet owners often need quick, safe guidance during uncertain moments, and AI can support that decision-making process when paired with retrieval, guardrails, and clear fallback behavior.

The system is intentionally narrow and safety-oriented: it focuses on pet-health support, retrieves relevant care guidance from a local knowledge base, and refuses to answer unrelated or unsafe requests. This reduces hallucination risk and keeps the assistant useful without pretending to replace veterinary care.

## Architecture Overview

The system follows a simple retrieval-augmented generation (RAG) workflow:

1. The user asks a pet-related question.
2. A guardrail checks whether the request is actually about pet care.
3. The retriever searches a local pet-care knowledge base for relevant guidance.
4. The AI agent reasons using that retrieved context before producing an answer.
5. The result is shown to the user and validated by basic automated checks and human review.

The Mermaid source for the architecture is in [diagrams/architecture.mmd](diagrams/architecture.mmd). It shows the flow from user input to retrieval, reasoning, output, and testing review.

## Project Structure

- [app.py](app.py) — command-line interface for the assistant
- [pawpal/rag.py](pawpal/rag.py) — retrieval and response logic
- [pawpal/__init__.py](pawpal/__init__.py) — package exports
- [data/pet_care_knowledge.txt](data/pet_care_knowledge.txt) — pet-care knowledge base
- [diagrams/architecture.mmd](diagrams/architecture.mmd) — Mermaid architecture diagram
- [tests/test_rag.py](tests/test_rag.py) — validation tests
- [requirements.txt](requirements.txt) — Python dependencies

## Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/connortully-prof/applied-ai-system-project.git
cd applied-ai-system-project
```

### 2. Create a virtual environment

On Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

On macOS/Linux:

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the app

```bash
python app.py
```

You can also pass a query directly:

```bash
python app.py "My dog has a fever and seems weak. What should I do?"
```

### 5. Run tests

```bash
python -m pytest -q
```

## Sample Interactions

### Example 1: Urgent symptoms

Input:

```text
My dog has a fever and seems weak. What should I do?
```

Output:

```text
PawPal: Based on the retrieved pet care guidance, this situation needs prompt veterinary attention. If your pet has a fever, weakness, breathing trouble, collapse, or severe symptoms, contact an emergency vet immediately. Keep your pet calm, stop exercise, and avoid giving human medication without veterinary advice.
```

### Example 2: Wellness question

Input:

```text
My cat is not eating and seems tired.
```

Output:

```text
PawPal: Based on the retrieved pet care guidance, start with the safest next steps: monitor symptoms closely, maintain hydration, avoid sudden diet changes, and contact a vet if the issue persists or worsens.
```

### Example 3: Non-pet query safety check

Input:

```text
How do I fix my car engine?
```

Output:

```text
This assistant is designed for pet care guidance only. Please ask about a dog, cat, or other pet health issue.
```

These examples demonstrate that the app is active, purpose-aware, and designed to support pet-specific decision-making instead of making generic or unsafe claims.

## Design Decisions

I built PawPal as a small, local, retrieval-based system rather than a large external API-driven chatbot because it keeps the project reproducible, understandable, and controllable. The design makes the system easier to run in a portfolio or classroom environment, while still demonstrating a genuine AI workflow: retrieve context, apply guardrails, and generate a safer answer.

### Trade-offs

- Strength: the system is transparent and easy to test.
- Strength: the knowledge base is local and easy to inspect or revise.
- Trade-off: it uses a lightweight, static knowledge set rather than a full production veterinary database.
- Trade-off: the assistant is intentionally conservative and avoids overconfident recommendations in medical situations.

This is a deliberate choice: for a pet-health assistant, reliability and safety matter more than being overly broad or conversational.

## Testing Summary

This project includes measurable reliability checks. I validated the behavior with automated tests and runtime verification, and the results are concrete rather than anecdotal.

> 2 out of 2 automated tests passed; the system correctly answered pet-care queries and rejected unrelated requests. The CLI also ran successfully in direct-query mode after fixing EOF handling.

### Automated tests

The project includes [tests/test_rag.py](tests/test_rag.py), which validates the two most important behaviors:

- a pet-care question returns a response that includes veterinary guidance,
- a non-pet question triggers the guardrail.

Current result:

```text
2 passed in 0.02s
```

### Runtime and logging checks

The app logs retrieval activity and errors using Python logging. This records system behavior when it loads the knowledge base and when it generates output. It also fails gracefully instead of crashing in invalid or edge-case situations.

### Human evaluation (structured)

I also reviewed the system output with a basic human evaluation table to confirm the assistant behaves safely and usefully.

| Test Input | Evaluation Criteria | Result |
| --- | --- | --- |
| "My dog has a fever and seems weak. What should I do?" | Provides urgent pet-care guidance and mentions veterinary attention | Pass |
| "My cat is not eating and seems tired." | Gives cautious, practical guidance without overconfidence | Pass |
| "How do I fix my car engine?" | Rejects as out of scope and explains the intended use | Pass |
| Empty input | Handles gracefully without crashing | Pass |

### What worked

- The retrieval flow produced answers grounded in relevant pet-care guidance.
- The guardrail prevented unrelated prompts from being processed.
- The CLI interface worked in interactive mode and in one-shot command-line mode.

### What did not work initially

- The first version of the CLI crashed when no input was provided in a non-interactive session because it used `input()` without handling EOF.
- The project started without a proper package structure, which caused import errors until the application was organized correctly.

### What I learned

This project reinforced that a useful AI system is not just about model output; it is about data flow, system design, verification, and safety. A strong AI project includes a clear way to retrieve facts, a way to check whether the request is appropriate, and a way to test the system before claiming it works.

## Key Takeaways

This project taught me that AI is most useful when it is constrained to a clear problem and grounded in reliable information. In practical terms, I learned how important it is to design around validation, guardrails, and transparency rather than assuming a model will always produce safe or correct answers.

## Final Notes

PawPal is a focused example of a practical AI application: narrow scope, retrieval-based reasoning, and explicit safety checks. It is a strong portfolio project because it demonstrates software engineering, AI application design, and responsible behavior in a real-world domain.

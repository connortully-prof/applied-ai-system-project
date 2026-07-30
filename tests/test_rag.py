from pawpal.rag import PawPalRAGSystem


def test_rag_returns_pet_care_guidance():
    system = PawPalRAGSystem()
    answer = system.answer("My dog has a fever and seems weak. What should I do?")

    assert "vet" in answer.lower() or "emergency" in answer.lower()
    assert len(answer) > 80


def test_guardrail_rejects_non_pet_question():
    system = PawPalRAGSystem()
    answer = system.answer("How do I fix my car engine?")

    assert "pet care" in answer.lower() or "not a pet care" in answer.lower()

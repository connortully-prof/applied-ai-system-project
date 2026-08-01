from __future__ import annotations

from pawpal.rag import PawPalRAGSystem


TEST_CASES = [
    ("My dog has a fever and seems weak. What should I do?", True),
    ("My cat is not eating and seems tired.", True),
    ("How do I fix my car engine?", False),
]


def run_evaluation() -> None:
    system = PawPalRAGSystem()
    passed = 0

    for query, should_pass in TEST_CASES:
        answer = system.answer(query)
        if should_pass:
            result = "PASS" if "vet" in answer.lower() or "veterinary" in answer.lower() or "care guidance" in answer.lower() else "FAIL"
        else:
            result = "PASS" if "pet care" in answer.lower() or "dog" in answer.lower() or "cat" in answer.lower() else "FAIL"

        print(f"Query: {query}\nResult: {result}\nAnswer: {answer[:140]}\n")
        if result == "PASS":
            passed += 1

    print(f"Evaluation summary: {passed}/{len(TEST_CASES)} checks passed")


if __name__ == "__main__":
    run_evaluation()

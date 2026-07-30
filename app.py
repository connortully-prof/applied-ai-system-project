from __future__ import annotations

from pawpal.rag import PawPalRAGSystem


def main() -> None:
    system = PawPalRAGSystem()
    print("PawPal Pet Care Assistant")
    print("Ask about symptoms, care, diet, or general pet wellness. Type 'quit' to exit.\n")

    while True:
        prompt = input("You: ").strip()
        if not prompt or prompt.lower() in {"quit", "exit", "bye"}:
            print("Goodbye.")
            break

        response = system.answer(prompt)
        print(f"PawPal: {response}\n")


if __name__ == "__main__":
    main()

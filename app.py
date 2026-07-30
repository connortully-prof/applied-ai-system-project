from __future__ import annotations

import sys

from pawpal.rag import PawPalRAGSystem


def main() -> None:
    system = PawPalRAGSystem()

    if len(sys.argv) > 1:
        query = " ".join(sys.argv[1:]).strip()
        if query:
            print(f"PawPal: {system.answer(query)}")
            return

    print("PawPal Pet Care Assistant")
    print("Ask about symptoms, care, diet, or general pet wellness. Type 'quit' to exit.\n")

    while True:
        try:
            prompt = input("You: ").strip()
        except EOFError:
            print("\nGoodbye.")
            break

        if not prompt or prompt.lower() in {"quit", "exit", "bye"}:
            print("Goodbye.")
            break

        response = system.answer(prompt)
        print(f"PawPal: {response}\n")


if __name__ == "__main__":
    main()

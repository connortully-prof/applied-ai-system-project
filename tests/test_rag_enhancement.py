from pawpal.rag import PawPalRAGSystem


def test_rag_supports_multiple_knowledge_sources(tmp_path):
    puppy_file = tmp_path / "puppy_care.txt"
    puppy_file.write_text(
        "Puppy vaccination schedule: Puppies need age-appropriate vaccines and a vet check-up.\n"
        "Vaccination timing should be planned with a veterinarian.",
        encoding="utf-8",
    )

    kitten_file = tmp_path / "kitten_care.txt"
    kitten_file.write_text(
        "Kitten hydration: Kittens need clean water and well-balanced nutrition.\n"
        "Monitor appetite and energy if a kitten seems weak.",
        encoding="utf-8",
    )

    system = PawPalRAGSystem(knowledge_sources=[puppy_file, kitten_file])
    answer = system.answer("My puppy needs vaccine guidance and a checkup.")

    assert "vaccine" in answer.lower() or "veterinarian" in answer.lower()
    assert len(answer) > 80

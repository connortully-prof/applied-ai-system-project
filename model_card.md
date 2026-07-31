# Model Card: PawPal AI Pet Care Assistant

## Overview

PawPal is a lightweight, retrieval-based pet-care assistant designed to provide safe, practical guidance for common pet-health questions. It is intentionally narrow in scope and uses a local knowledge base rather than open-ended general advice generation.

## Intended Use

This system is intended for:

- general pet wellness questions,
- symptom awareness for common household pets,
- reminder-style pet-care guidance,
- safe suggestions that encourage veterinary evaluation when symptoms are serious.

This system is not intended to replace a licensed veterinarian or diagnose medical conditions.

## Responsible AI Reflection

I collaborated with AI as a coding and design partner during this project. It helped me structure the application, refine the retrieval workflow, and generate initial code for the project scaffold. I used it to speed up implementation and to test ideas quickly, but I remained responsible for validating the output, checking accuracy, and shaping the project around safety requirements.

### One helpful AI suggestion

A helpful suggestion from the AI was to include a guardrail that rejects non-pet requests and a retrieval layer that pulls relevant pet-care guidance before answering. That improved the project by reducing irrelevant responses and making the app behave more safely and purposefully.

### One flawed AI suggestion

One flawed suggestion was to assume the assistant could safely provide detailed medical treatment advice without a stronger safety boundary. I corrected that by narrowing the system to guidance and encouraging veterinary consultation when symptoms were urgent or unclear. This was a useful reminder that AI suggestions must be checked against domain risk and user safety.

## Limitations

- The knowledge base is small and static.
- It does not integrate with live veterinary sources or real-time data.
- It may miss edge cases or unusual symptoms.
- It should not be treated as a diagnostic tool.
- The system is designed for safe, educational guidance rather than medical certainty.

## Human Oversight

This project relies on humans to review outputs and interpret them responsibly. In real use, owners should consult a veterinarian for diagnosis, treatment plans, or urgent symptoms. The assistant should be treated as supportive, not definitive.

## Evaluation Summary

The project was tested with basic pet-related prompts and non-pet guardrail checks. These tests confirmed that the system behaves as designed in a narrow, controlled domain.

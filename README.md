# PawPal AI Pet Care Assistant

PawPal is a lightweight AI-powered pet care assistant built to help owners with common health, wellness, and care questions. It uses a retrieval-augmented generation (RAG) approach: before answering, it retrieves relevant pet-care guidance from a local knowledge base and incorporates that information into the response.

## AI Feature Included

This project includes a Retrieval-Augmented Generation (RAG) workflow:

- It retrieves relevant pet-care guidance from a local knowledge base.
- It filters out non-pet requests with a safety guardrail.
- It uses the retrieved context to produce safer, more useful advice.
- It logs activity and fails gracefully if an error occurs.

## Project Structure

- `app.py` — command-line interface for the assistant
- `pawpal/` — main application package
- `data/pet_care_knowledge.txt` — veterinary-style knowledge base
- `diagrams/architecture.mmd` — Mermaid architecture diagram
- `assets/` — architecture/export assets
- `tests/` — validation tests

## Setup

1. Open a terminal in the project folder.
2. Create a virtual environment:

   ```bash
   python -m venv .venv
   ```

3. Activate the environment:

   On Windows PowerShell:

   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```

   On macOS/Linux:

   ```bash
   source .venv/bin/activate
   ```

4. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Run the app:

   ```bash
   python app.py
   ```

6. Example prompts:

   ```text
   My dog has a fever and seems weak. What should I do?
   My cat is not eating and seems tired.
   How do I switch my pet to a new food?
   ```

## Testing

```bash
python -m pytest -q
```

## Safety and Logging

- Non-pet questions are rejected with a clear guardrail.
- User requests and errors are logged in the application logger.
- The system returns a safe fallback if it cannot answer reliably.

## Architecture

The Mermaid source file is in:

- `diagrams/architecture.mmd`

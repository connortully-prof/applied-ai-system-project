# AI Interaction Log

## RAG Enhancement

This project extends the core retrieval system by allowing multiple custom knowledge sources, not just one static file. The app combines all available pet-care documents before answering, so the assistant can retrieve guidance from more than one source and explain which information it used.

### Example before/after

Before:
- Only one knowledge file was loaded.
- Retrieval was limited to one static document.

After:
- The system accepts multiple knowledge sources.
- Each source contributes relevant entries to the retrieval pool.
- Answers include a confidence score based on the matching context.

## Evaluation summary

- Automated behavior tests pass for pet-care and guardrail cases.
- Confidence score is tracked in the output for each response.
- Logs record retrieval and answer generation events.

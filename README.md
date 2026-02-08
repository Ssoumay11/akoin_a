# LLM-Assisted COREP Reporting Assistant (Prototype)

## Executive Summary

This project demonstrates how Retrieval-Augmented Generation (RAG) with an open-source LLM can assist UK banks in preparing PRA COREP regulatory reports.

The prototype focuses on the COREP C01.00 (Own Funds) template and shows an end-to-end workflow:

User Question → Regulatory Retrieval → Structured LLM Output → Template-Aligned JSON

The system grounds all responses in official regulatory text to reduce hallucination risk and improve explainability.

---

## Business Problem

Preparing COREP returns requires:

- Interpreting complex PRA Rulebook provisions
- Mapping capital definitions (CET1, AT1, Tier 2) to correct template rows
- Justifying reported figures using regulatory references

Manual processes are time-consuming and error-prone.

This prototype explores how LLMs can assist by:

- Identifying correct reporting rows
- Mapping financial values to template fields
- Providing regulatory justification

---

## Key Features

- Open-source LLM (Llama 3 via Groq)
- Retrieval-Augmented Generation (RAG)
- Regulation-aware chunking (Article + Row based)
- FAISS semantic search
- Structured JSON output aligned to COREP C01.00
- Deterministic, low-temperature responses

---

## System Architecture

1. Regulatory PDFs are converted into text.
2. Text is chunked by legal structure (Articles and template rows).
3. Embeddings are generated using Sentence Transformers.
4. FAISS provides semantic retrieval.
5. Retrieved regulatory context is passed to Llama 3.
6. The model generates structured JSON aligned with COREP schema.

This design ensures regulatory grounding and traceability.

---

## Technology Stack

- Python
- Sentence-Transformers (all-MiniLM-L6-v2)
- FAISS (vector search)
- Groq API (Llama 3)
- PyMuPDF (PDF extraction)

---

## How to Run

### Install dependencies

```bash
pip install pymupdf sentence-transformers faiss-cpu numpy groq

Set Groq API key

Windows (PowerShell):
$env:GROQ_API_KEY="your_api_key"

Run the pipeline
python extract_text.py
python chunker.py
python app.py

# Ask question
query = "In COREP C01.00 template, where should 50 million CET1 capital be reported?"

===== LLM OUTPUT =====

{
  "template": "C01.00",
  "fields": [
    {
      "row_code": "0450",
      "field_name": "15.1 Direct holdings of CET1 capital of financial sector entities where the institution has a significant investment",
      "value": "50,000,000",
      "justification": "The question asks where 50 million CET1 capital should be reported. Given the context, row 0450 is for direct holdings of CET1 capital of financial sector entities where the institution has a significant investment, which matches the description of the amount to be reported."
    }
  ]
}

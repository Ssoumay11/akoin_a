import re
import json
import os


def chunk_by_article(text):
    pattern = r"(Article\s\d+.*?)(?=Article\s\d+|\Z)"
    matches = re.findall(pattern, text, re.DOTALL)
    return matches


def chunk_by_row(text):
    pattern = r"(\d{4}\s.*?)(?=\n\d{4}\s|\Z)"
    matches = re.findall(pattern, text, re.DOTALL)
    return matches


def save_chunks(chunks, source_name, output_path):
    structured = []

    for i, chunk in enumerate(chunks):
        structured.append({
            "id": f"{source_name}_{i}",
            "source": source_name,
            "text": chunk.strip()
        })

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(structured, f, indent=2)

    print(f"✅ Saved {len(chunks)} chunks to {output_path}")


if __name__ == "__main__":

    os.makedirs("data/chunks", exist_ok=True)

    # PRA
    with open("data/processed/pra_own_funds.txt", "r", encoding="utf-8") as f:
        pra_text = f.read()

    pra_chunks = chunk_by_article(pra_text)
    save_chunks(pra_chunks, "PRA", "data/chunks/pra_chunks.json")

    # COREP
    with open("data/processed/corep_c01_instructions.txt", "r", encoding="utf-8") as f:
        corep_text = f.read()

    corep_chunks = chunk_by_row(corep_text)
    save_chunks(corep_chunks, "COREP", "data/chunks/corep_chunks.json")

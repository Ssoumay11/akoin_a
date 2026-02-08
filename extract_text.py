import fitz  # pymupdf

def extract_text_from_pdf(pdf_path, output_txt):
    doc = fitz.open(pdf_path)
    full_text = ""

    for page in doc:
        full_text += page.get_text()

    with open(output_txt, "w", encoding="utf-8") as f:
        f.write(full_text)

    print(f"Extracted text saved to {output_txt}")


if __name__ == "__main__":
    extract_text_from_pdf(
        "data/raw/pra_own_funds_rules.pdf",
        "data/processed/pra_own_funds.txt"
    )

    extract_text_from_pdf(
        "data/raw/corep_own_funds_instructions.pdf",
        "data/processed/corep_c01_instructions.txt"
    )

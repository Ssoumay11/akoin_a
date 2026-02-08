from retriever import load_chunks, build_index, retrieve
from llm_engine import generate_response

# Load chunk data
pra_chunks = load_chunks("data/chunks/pra_chunks.json")
corep_chunks = load_chunks("data/chunks/corep_chunks.json")

all_chunks = pra_chunks + corep_chunks

# Build FAISS index
index, texts = build_index(all_chunks)

# Ask question
query = "In COREP C01.00 template, where should 50 million CET1 capital be reported?"

# Retrieve relevant regulation

retrieved_context = retrieve(query, index, texts, k=8)

context_text = "\n\n".join(retrieved_context)


# Generate LLM response
response = generate_response(context_text, query)

print("\n===== LLM OUTPUT =====\n")
print(response)

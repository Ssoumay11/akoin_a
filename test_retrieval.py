from retriever import load_chunks, build_index, retrieve

# Load chunk files
pra_chunks = load_chunks("data/chunks/pra_chunks.json")
corep_chunks = load_chunks("data/chunks/corep_chunks.json")

# Combine both sources
all_chunks = pra_chunks + corep_chunks

# Build vector index
index, texts = build_index(all_chunks)

# Test query
query = "Where should Common Equity Tier 1 capital be reported in C01?"

results = retrieve(query, index, texts)

print("\n🔍 Retrieved Context:\n")
for r in results:
    print("-----")
    print(r[:500])  # print first 500 characters

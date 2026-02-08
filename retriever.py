import json
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# Load embedding model
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")


def load_chunks(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def build_index(all_chunks):
    texts = [chunk["text"] for chunk in all_chunks]

    print("🔹 Creating embeddings...")
    embeddings = embedding_model.encode(texts, show_progress_bar=True)

    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(np.array(embeddings))

    print("FAISS index built.")
    return index, texts


def retrieve(query, index, texts, k=5):
    query_embedding = embedding_model.encode([query])
    distances, indices = index.search(np.array(query_embedding), k)

    results = []
    for i in indices[0]:
        results.append(texts[i])

    return results

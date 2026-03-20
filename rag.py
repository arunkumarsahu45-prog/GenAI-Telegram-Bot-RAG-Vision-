from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

documents = [
    "AI is transforming industries.",
    "Machine learning is a subset of AI.",
    "RAG combines retrieval and generation.",
]

embeddings = model.encode(documents)

index = faiss.IndexFlatL2(384)
index.add(np.array(embeddings))

def retrieve(query):
    q_emb = model.encode([query])
    D, I = index.search(np.array(q_emb), k=2)
    return [documents[i] for i in I[0]]


import subprocess

def generate_answer(context, query):
    prompt = f"""
    Context: {context}
    Question: {query}
    Answer clearly:
    """

    result = subprocess.run(
        ["ollama", "run", "mistral"],
        input=prompt.encode(),
        capture_output=True
    )

    return result.stdout.decode()
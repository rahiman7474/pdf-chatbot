import faiss
import numpy as np
import pickle
from sentence_transformers import SentenceTransformer
from transformers import AutoTokenizer, AutoModelForCausalLM

# Embedding model
embedder = SentenceTransformer("BAAI/bge-base-en-v1.5")

# Language model for answering
# tokenizer = AutoTokenizer.from_pretrained("tiiuae/falcon-7b-instruct")
# model = AutoModelForCausalLM.from_pretrained("tiiuae/falcon-7b-instruct")

tokenizer = AutoTokenizer.from_pretrained("facebook/bart-large")
model = AutoModelForSeq2SeqLM.from_pretrained("facebook/bart-large")



def create_vector_store(chunks, index_path="data/index.faiss", meta_path="data/chunks.pkl"):
    embeddings = embedder.encode(chunks)
    dim = embeddings[0].shape[0]
    index = faiss.IndexFlatL2(dim)
    index.add(np.array(embeddings))
    faiss.write_index(index, index_path)
    with open(meta_path, "wb") as f:
        pickle.dump((chunks, embeddings), f)
    return index, embeddings

def load_vector_store(index_path="data/index.faiss", meta_path="data/chunks.pkl"):
    index = faiss.read_index(index_path)
    with open(meta_path, "rb") as f:
        chunks, embeddings = pickle.load(f)
    return index, chunks, embeddings

def retrieve(context_chunks, index, question, embeddings, top_k=5):
    question_embedding = embedder.encode([question])
    D, I = index.search(np.array(question_embedding), k=top_k)
    return [context_chunks[i] for i in I[0]]

def answer_question_rag(chunks, question):
    context = "\n".join(chunks[:5])
    prompt = f"Use the context below to answer the question:\n\nContext:\n{context}\n\nQuestion: {question}\nAnswer:"
    inputs = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=1024)
    outputs = model.generate(**inputs, max_new_tokens=200)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

import streamlit as st
import os
from pdf_utils import extract_text_from_pdf, split_text
from rag_utils import create_vector_store, load_vector_store, retrieve, answer_question_rag

PDF_PATH = "data/rahiman_bio_story.pdf"
INDEX_PATH = "data/indexRahiman.faiss"
CHUNKS_PATH = "data/chunksRahiman.pkl"

st.set_page_config(page_title="PDF Chatbot")
st.title("U can ask anything about Rahiman")

# Load or create index
if "index" not in st.session_state:
    if os.path.exists(INDEX_PATH) and os.path.exists(CHUNKS_PATH):
        st.info("Loading cached index...")
        index, chunks, embeddings = load_vector_store(INDEX_PATH, CHUNKS_PATH)
    else:
        st.info("Processing PDF...")
        raw_text = extract_text_from_pdf(PDF_PATH)
        chunks = split_text(raw_text, chunk_size=500, overlap=50)
        index, embeddings = create_vector_store(chunks)
    st.session_state.index = index
    st.session_state.chunks = chunks
    st.session_state.embeddings = embeddings
    st.success("Ready!")

# Preview raw extracted text
# if st.checkbox("Preview Extracted Text"):
#     st.text_area("Raw Text", extract_text_from_pdf(PDF_PATH), height=300)

# Ask a question
question = st.text_input("Ask your question:")
if question:
    context = retrieve(
        st.session_state.chunks,
        st.session_state.index,
        question,
        st.session_state.embeddings,
        top_k=5
    )

    # if st.checkbox("Show Retrieved Context"):
    #     st.markdown("**Context Used:**")
    #     st.text("\n\n".join(context))

    answer = answer_question_rag(context, question)
    st.markdown(f"**Answer:** {answer}")


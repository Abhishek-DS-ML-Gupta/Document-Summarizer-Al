import streamlit as st
from src.loader import load_pdf
from src.splitter import split_text
from src.embedder import create_vector_store
from src.summarizer import summarize_query

st.set_page_config(page_title="AI Legal Document Summarizer", layout="wide")

st.title("⚖️ AI Legal Document Summarizer")
st.write("Upload legal documents (contracts, case laws, etc.) to summarize using GPT-4 + FAISS.")

uploaded_file = st.file_uploader("📄 Upload a PDF", type=["pdf"])

if uploaded_file:
    with st.spinner("Extracting text..."):
        text = load_pdf(uploaded_file)
        chunks = split_text(text)
        db = create_vector_store(chunks)
        st.success(f"✅ Loaded {len(chunks)} text chunks.")

    query = st.text_input("💬 Ask a question about this document (or type 'summarize'):")

    if query:
        with st.spinner("Generating summary..."):
            result = summarize_query(db, query)
            st.subheader("📘 Summary / Answer:")
            st.write(result)

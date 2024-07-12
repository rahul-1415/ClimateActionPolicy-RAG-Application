import streamlit as st
from components.retriever import initialize_retriever
from components.generator import create_context_from_docs, generate_with_ollama3

st.title("Climate Policy RAG System")

query = st.text_input("Enter your query:")

if query:
    # Initialize retriever
    retriever = initialize_retriever()

    # Retrieve documents
    retrieved_docs = retriever.invoke(query)
    st.write("Retrieved Documents:", retrieved_docs)

    # Create context from retrieved documents
    context = create_context_from_docs(retrieved_docs)

    # Generate answer
    answer = generate_with_ollama3(context, query)
    st.write("Generated Response:", answer)

from langchain_community.embeddings import HuggingFaceBgeEmbeddings
from langchain_chroma import Chroma
from pathlib import Path
import os
import chromadb

def initialize_retriever():
    # Set the absolute path for the Chroma database
    ABS_PATH = Path().resolve().joinpath('Chroma')
    DB_DIR = os.path.join(ABS_PATH, "env_policy")

    # Define client settings for Chroma
    client_settings = chromadb.config.Settings(
        is_persistent=True,
        persist_directory=DB_DIR,
        anonymized_telemetry=False,
    )

    # Initialize the HuggingFaceBgeEmbeddings with the correct model
    embedder = HuggingFaceBgeEmbeddings(model_name="BAAI/bge-small-en")

    # Load the Chroma vector store
    bge_vectorstore = Chroma(
        embedding_function=embedder,
        client_settings=client_settings,
        collection_name="env_policy_bge",
        collection_metadata={"hnsw": "cosine"}
    )

    # Initialize retriever
    retriever = bge_vectorstore.as_retriever(
        search_type="mmr",
        search_kwargs={"k": 5, "include_metadata": True}
    )

    return retriever

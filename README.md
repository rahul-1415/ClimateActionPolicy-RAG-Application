# ClimateActionPolicy-RAG-Application

## Overview

ClimateActionPolicy-RAG-Application is a project designed to support climate action policy recommendations using a Retrieval-Augmented Generation (RAG) system. The application leverages a retrieval component to fetch relevant documents and a generative model to create contextually enriched responses based on the retrieved documents.

## Features

- **Streamlit Interface**: Provides an interactive web interface for querying and displaying responses.
- **Document Retrieval**: Utilizes a retriever to fetch relevant documents based on user queries.
- **Contextual Response Generation**: Generates responses using the Ollama LLaMA 3 model, enriched with context from retrieved documents.
- **Chat History Management**: Supports managing multiple chat sessions and maintaining chat histories.

## Files

- **app.py**: Main Streamlit application file that sets up the web interface and handles user interactions.
- **requirements.txt**: Lists all the Python dependencies required to run the application.

## Folders

- **Chroma**: Directory for the Chroma database used for document retrieval.
- **components**: Contains the retrieval and generation modules.
  - **generator.py**: Handles response generation using the Ollama LLaMA 3 model.
  - **retriever.py**: Manages document retrieval using Chroma and HuggingFace embeddings.


### Running the Application

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/your-username/ClimateActionPolicy-RAG-Application.git
    cd ClimateActionPolicy-RAG-Application
    ```

2. **Create and Activate a Virtual Environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the Required Packages**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Start the Streamlit Application**:
    ```bash
    streamlit run app.py
    ```
    Open your web browser and navigate to `http://localhost:8501`.

## Dependencies

The following Python packages are required to run the application:

- streamlit
- langchain
- langchain_community
- chromadb
- transformers
- torch
- pandas
- langchain_chroma
- sentence_transformers

Install the required packages using pip:

```bash
pip install -r requirements.txt

import streamlit as st
from components.retriever import initialize_retriever
from components.generator import create_context_from_docs, generate_with_ollama3

# Initialize session state variables for chat history if they don't exist
if "all_chats" not in st.session_state:
    st.session_state.all_chats = []

if "current_chat" not in st.session_state:
    st.session_state.current_chat = []

# Function to start a new chat
def new_chat():
    if st.session_state.current_chat:
        st.session_state.all_chats.append(st.session_state.current_chat)
    st.session_state.current_chat = []

# Layout the page with two columns
col1, col2 = st.columns([1, 3])

with col1:
    st.title("Chats")
    st.button("New Chat", on_click=new_chat)
    st.subheader("Chat History:")
    for i, chat in enumerate(st.session_state.all_chats):
        if st.button(f"Chat {i + 1}"):
            st.session_state.current_chat = chat

with col2:
    st.title("Climate Policy RAG System")

    # Display chat history
    for chat in st.session_state.current_chat:
        with st.chat_message(chat["role"]):
            st.markdown(chat["content"])

    # User input for query
    if prompt := st.chat_input("Enter your query:"):
        # Initialize retriever
        retriever = initialize_retriever()

        # Retrieve documents
        retrieved_docs = retriever.invoke(prompt)

        # Display retrieved documents in a scrollable box with black text
        with st.chat_message("user"):
            st.markdown(f"**User:** {prompt}")
            st.markdown(
                """
                <div style="height: 200px; overflow-y: scroll; padding: 10px; border: 1px solid #ddd; background-color: #f9f9f9; border-radius: 5px; color: black;">
                """
                +
                "".join([f"<div style='margin-bottom: 10px;'><strong>Document {i+1}:</strong><br>{doc}</div>" for i, doc in enumerate(retrieved_docs)])
                +
                """
                </div>
                """,
                unsafe_allow_html=True
            )

        # Create context from retrieved documents
        context = create_context_from_docs(retrieved_docs)

        # Generate answer
        answer = generate_with_ollama3(context, prompt)

        # Update chat history
        st.session_state.current_chat.append({"role": "user", "content": prompt})
        st.session_state.current_chat.append({"role": "assistant", "content": answer})

        # Display assistant response
        with st.chat_message("assistant"):
            st.markdown(answer)

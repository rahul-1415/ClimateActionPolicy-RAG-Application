from langchain_community.llms import Ollama

def create_context_from_docs(docs):
    return " ".join([doc.page_content for doc in docs])

def generate_with_ollama3(context, question):
    llm = Ollama(model='llama3')
    input_text = f"{context} {question}"
    result = llm.invoke(input_text)
    return result

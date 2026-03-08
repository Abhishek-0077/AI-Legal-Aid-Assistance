from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
import os
from groq import Groq

# Initialize embedding model
embedding_model = HuggingFaceEmbeddings(
    model_name="BAAI/bge-small-en-v1.5"
)

# Define persist directory
persist_directory = r"C:\Users\abhishek\Downloads\SIC_Project\vector_db\vector_db\legal_bot_database"

# Create Chroma vector store instance
# Note: If the directory exists, Chroma will load the existing collection.
# If it doesn't exist, it will create a new one.
vector_store = Chroma(persist_directory=persist_directory, embedding_function=embedding_model)
retriever = vector_store.as_retriever(search_type="similarity", search_kwargs={"k": 5})

# ---------------------------------------------
# Initialize Groq API
# ---------------------------------------------
client = Groq(
    api_key="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"
)

# ---------------------------------------------
# Legal Aid Assistant Function
# ---------------------------------------------
def legal_assistant(question):
    # -------- STEP 1: Check if question is legal --------
    legal_keywords = [
        "law","legal","court","judge","crime","criminal","ipc","crpc",
        "constitution","rights","police","arrest","bail","fir",
        "punishment","section","act","consumer","rti","property",
        "divorce","custody","tax","fraud","cheating","murder","right"
    ]

    is_legal = any(word in question.lower() for word in legal_keywords)

    if not is_legal:
        return "Please ask relevant questions related to legal aid only."

    # -------- STEP 2: Retrieve RAG documents --------
    docs = retriever.invoke(question)

    context = "\n".join([doc.page_content for doc in docs])

    # -------- STEP 3: Prompt building --------
    if context.strip():

        prompt = f"""
You are an AI Legal Aid Assistant.

Use the provided legal context to answer the question clearly.

Legal Context:
{context}

User Question:
{question}

Give a clear legal explanation.
"""

    else:

        # If context not found but question is legal
        prompt = f"""
You are an AI Legal Aid Assistant for Indian law.

The user asked a legal question but no specific context was retrieved.
Answer using general legal knowledge about Indian law.

User Question:
{question}

Give a clear legal explanation.
"""

    # -------- STEP 4: Call LLM --------
    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {"role": "system", "content": "You are a professional legal aid assistant specialized in Indian law."},
            {"role": "user", "content": prompt+"\n\nAnswer in a clear and concise manner."}
        ],
        temperature=0
    )

    return response.choices[0].message.content

print("Embedding model and Chroma vector store initialized successfully.")
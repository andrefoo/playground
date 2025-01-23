from langchain_fireworks import FireworksEmbeddings
from langchain_core.vectorstores import InMemoryVectorStore
from dotenv import load_dotenv
import numpy as np
import os

def create_embeddings():
    # Load environment variables
    load_dotenv()
    
    # Check if API key exists
    api_key = os.getenv("FIREWORKS_API_KEY")
    if not api_key:
        raise ValueError(
            "FIREWORKS_API_KEY not found in environment variables. "
            "Please make sure you have created a .env file with your API key"
        )

    # Initialize the Fireworks embeddings model
    embeddings = FireworksEmbeddings(
        fireworks_api_key=api_key,
        model="nomic-ai/nomic-embed-text-v1.5",
    )
    return embeddings

def cosine_similarity(v1, v2):
    """Calculate cosine similarity between two vectors."""
    dot_product = np.dot(v1, v2)
    norm1 = np.linalg.norm(v1)
    norm2 = np.linalg.norm(v2)
    return dot_product / (norm1 * norm2)

def demonstrate_embeddings():
    try:
        embeddings = create_embeddings()
        
        # Sample texts
        text1 = "LangChain is the framework for building context-aware reasoning applications"
        text2 = "LangGraph is a library for building stateful, multi-actor applications with LLMs"
        
        print("\n1. Single Text Embedding:")
        single_vector = embeddings.embed_query(text1)
        print(f"Vector preview: {str(single_vector)[:100]}...")
        
        print("\n2. Multiple Text Embeddings:")
        two_vectors = embeddings.embed_documents([text1, text2])
        for i, vector in enumerate(two_vectors, 1):
            print(f"Text {i} vector preview: {str(vector)[:100]}...")
        
        # Calculate and display similarity
        print("\n3. Cosine Similarity between texts:")
        similarity = cosine_similarity(two_vectors[0], two_vectors[1])
        print(f"Similarity between text1 and text2: {similarity:.4f}")
        
        print("\n4. Vector Store Retrieval:")
        # Create and query a vector store
        vectorstore = InMemoryVectorStore.from_texts(
            [text1, text2],
            embedding=embeddings,
        )
        retriever = vectorstore.as_retriever()
        retrieved_documents = retriever.invoke("What is LangChain?")
        print(f"Retrieved text: {retrieved_documents[0].page_content}")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    print("Demonstrating Fireworks Embeddings with LangChain")
    print("=" * 50)
    demonstrate_embeddings()

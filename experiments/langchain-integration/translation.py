from langchain_fireworks import ChatFireworks
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os

def main():
    # Load environment variables
    load_dotenv()
    
    # Check if API key exists
    api_key = os.getenv("FIREWORKS_API_KEY")
    if not api_key:
        raise ValueError(
            "FIREWORKS_API_KEY not found in environment variables. "
            "Please make sure you have created a .env file with your API key"
        )

    # Initialize the chat model
    llm = ChatFireworks(
        fireworks_api_key=api_key,
        model="accounts/fireworks/models/llama-v3-8b-instruct"
    )
    
    # Create the translation prompt template
    prompt = ChatPromptTemplate.from_messages([
        (
            "system",
            "You are a helpful assistant that translates {input_language} to {output_language}.",
        ),
        ("human", "{input}"),
    ])

    # Create the chain
    chain = prompt | llm

    # Test the translation
    response = chain.invoke({
        "input_language": "English",
        "output_language": "German",
        "input": "I love programming.",
    })
    
    print("Translation result:")
    print(response.content)

if __name__ == "__main__":
    main() 
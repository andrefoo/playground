from fireworks.client import Fireworks
from dotenv import load_dotenv
import os

def initialize_client():
    """Initialize the Fireworks client."""
    load_dotenv()
    return Fireworks(api_key=os.getenv("FIREWORKS_API_KEY"))

def override_system_prompt(messages, new_system_prompt):
    """
    Override the system prompt in the message list.
    If no system prompt exists, add it at the beginning.
    """
    messages = [msg for msg in messages if msg["role"] != "system"]
    messages.insert(0, {
        "role": "system",
        "content": new_system_prompt
    })
    return messages

def chat():
    """Run the interactive chat session."""
    client = initialize_client()
    
    # Initialize conversation with default system prompt
    messages = [{
        "role": "system",
        "content": "You are a pirate."
    }]
    
    print("ChatBot initialized! Special commands:")
    print("- Type '/system <new prompt>' to override the system prompt")
    print("- Type '/exit' to end the conversation")
    print("- Type '/history' to see the conversation history")
    print("\nStart chatting!")
    
    while True:
        user_input = input("\nYou: ").strip()
        
        # Handle special commands
        if user_input.lower() == '/exit':
            print("Goodbye!")
            break
            
        elif user_input.lower() == '/history':
            print("\nConversation History:")
            for msg in messages:
                if msg["role"] != "system":
                    print(f"{msg['role'].title()}: {msg['content']}")
            continue
            
        elif user_input.lower().startswith('/system '):
            new_prompt = user_input[8:].strip()
            messages = override_system_prompt(messages, new_prompt)
            print(f"System prompt updated to: {new_prompt}")
            continue
            
        # Add user message to history
        messages.append({
            "role": "user",
            "content": user_input
        })
        
        try:
            # Get response from model
            response = client.chat.completions.create(
                model="accounts/fireworks/models/llama-v3-8b-instruct",
                messages=messages,
                stream=True
            )
            
            # Process and store assistant's response using streaming
            print("\nAssistant: ", end="", flush=True)
            assistant_response = ""
            for chunk in response:
                if chunk.choices[0].delta.content is not None:
                    content = chunk.choices[0].delta.content
                    print(content, end="", flush=True)
                    assistant_response += content
            
            messages.append({
                "role": "assistant",
                "content": assistant_response
            })
            
        except Exception as e:
            print(f"\nError: {str(e)}")
            messages.pop()  # Remove the failed message from history

if __name__ == "__main__":
    chat()
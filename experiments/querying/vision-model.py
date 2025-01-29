import fireworks.client
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Set the API key for authentication
fireworks.client.api_key = os.getenv("FIREWORKS_API_KEY")

# Create a chat completion request using the Fireworks API
response = fireworks.client.ChatCompletion.create(
  # Specify the vision-capable model to use
  model = "accounts/fireworks/models/phi-3-vision-128k-instruct",
  
  # Define the messages array with user input
  messages = [{
    "role": "user",  # Indicate this is a user message
    "content": [{
      # First content item: the text prompt
      "type": "text",
      "text": "Can you describe this image?",
    }, {
      # Second content item: the image to analyze
      "type": "image_url",
      "image_url": {
        "url": "https://images.unsplash.com/photo-1582538885592-e70a5d7ab3d3?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1770&q=80"
      },
    }, ],
  }],
)

# Print the model's response
print(response.choices[0].message.content)

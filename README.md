# Playground

This is a playground repository for experimenting with Fireworks API.

## Getting Started

This repository is meant for:
- Testing new ideas
- Familiarizing with Fireworks API
- Learning new programming concepts
- Experimenting with different technologies 

## Setup
1. Clone the repository
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - Unix/macOS: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Create a `.env` file with your Fireworks API key:
   ```
   FIREWORKS_API_KEY=your-api-key-here
   ```

## Experiments

### 1. Langchain Integration
Located in `experiments/langchain-integration/`
- Basic integration of Fireworks API with LangChain
- Environment setup and connection testing

### 2. Image Generation
Located in `experiments/image-generation/`
- Text-to-image generation using Stable Diffusion XL
- Image-to-image modifications
- ControlNet experiments for guided image generation

Examples:
- `generate-image.py`: Create images from text prompts
- `image-to-image.py`: Modify existing images with new prompts
- `controlnet.py`: Use ControlNet for structured image generation

### 3. Model Querying
Located in `experiments/querying/`
- Text model interactions with customizable system prompts
- Vision model capabilities for image analysis
- Interactive chat sessions with model responses

Examples:
- `text-model.py`: Interactive chat with customizable system prompts
- `vision-model.py`: Image analysis using Phi-3 Vision model 

### 4. Chatbot Implementation
Located in `chatbot/`
- EXTREMELY SIMPLE real-time chat interface using FastAPI and WebSocket
- Streaming responses from Mixtral-8x7b-instruct model
- Interactive web interface with dynamic message updates

Relevant files:
- `main.py`: FastAPI server with WebSocket implementation
- `templates/chat.html`: Frontend chat interface

## Running the Chatbot
1. Navigate to the chatbot directory
2. Run the FastAPI server: `uvicorn chatbot.main:app --reload`
3. Open `http://localhost:8000` in your browser 
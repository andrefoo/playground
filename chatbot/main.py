from fastapi import FastAPI, Request, WebSocket
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import fireworks.client
import os
import json

# Initialize FastAPI app
app = FastAPI()

# Mount static files
app.mount("/static", StaticFiles(directory="chatbot/static"), name="static")

# Initialize templates
templates = Jinja2Templates(directory="chatbot/templates")

# Initialize Fireworks client
fireworks.client.api_key = os.getenv("FIREWORKS_API_KEY")

class ChatMessage(BaseModel):
    message: str

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("chat.html", {"request": request})

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    
    try:
        while True:
            # Receive message from client
            data = await websocket.receive_text()
            message = json.loads(data)["message"]

            try:
                # Call Fireworks chat model with streaming
                completion = fireworks.client.ChatCompletion.create(
                    model="accounts/fireworks/models/mixtral-8x7b-instruct",
                    messages=[
                        {"role": "user", "content": message}
                    ],
                    max_tokens=1000,
                    temperature=0.7,
                    stream=True  # Enable streaming
                )

                # Stream the response
                full_response = ""
                for chunk in completion:
                    if hasattr(chunk.choices[0], 'delta') and chunk.choices[0].delta.content is not None:
                        content = chunk.choices[0].delta.content
                        full_response += content
                        # Send each chunk to the client
                        await websocket.send_json({
                            "type": "chunk",
                            "content": content
                        })

                # Send completion message
                await websocket.send_json({
                    "type": "complete",
                    "content": full_response
                })

            except Exception as e:
                # Send error message
                await websocket.send_json({
                    "type": "error",
                    "content": str(e)
                })

    except Exception as e:
        print(f"WebSocket error: {e}")
        # Client disconnected or other error occurred
        pass 
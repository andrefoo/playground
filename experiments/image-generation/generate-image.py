import fireworks.client
from fireworks.client.image import ImageInference, Answer
from PIL import Image
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize the ImageInference client
fireworks.client.api_key = os.getenv("FIREWORKS_API_KEY")
inference_client = ImageInference(model="stable-diffusion-xl-1024-v1-0")

# Generate an image using the text_to_image method
answer : Answer = inference_client.text_to_image(
    prompt="A beautiful sunset over the ocean with a car freely floating in the water",
    negative_prompt="fish, boat",
    cfg_scale=7,
    height=1024,
    width=1024,
    sampler="K_EULER", # use K_DPMPP_2M for higher quality, K_EULER for faster
    samples=1,
    steps=50,
    seed=0,
    safety_check=False, #IMPORTANT FOR PRODUCTION
)

if answer.image is None:
  raise RuntimeError(f"No return image, {answer.finish_reason}")
else:
  answer.image.save("output.jpg")
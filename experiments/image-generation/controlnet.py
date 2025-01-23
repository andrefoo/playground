# pip install 'fireworks-ai>=0.8.0', Pillow
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

# Modify an existing image using the control_net method
answer : Answer = inference_client.control_net(
    control_image="output.jpg",
    control_net_name="canny",
    conditioning_scale=0.2,
    prompt="A beautiful sunset over the ocean with a car freely floating in the water, a light rain falling over the ocean",
    cfg_scale=5,
    sampler=None,
    steps=30,
    seed=0,
    safety_check=False,
    output_image_format="JPG",
    # Add additional parameters here as necessary
)

if answer.image is None:
  raise RuntimeError(f"No return image, {answer.finish_reason}")
else:
  answer.image.save("output_controlnet.jpg")
import fireworks.client
from fireworks.client.image import ImageInference, Answer
from PIL import Image
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize the ImageInference client
fireworks.client.api_key = os.getenv("FIREWORKS_API_KEY")
inference_client = ImageInference(model="playground-v2-1024px-aesthetic")

# Modify an existing image using the image_to_image method
answer : Answer = inference_client.image_to_image(
    init_image="output.jpg",
    prompt="a bear beside the car",
    image_strength=0.3,
    cfg_scale=5,
    sampler="K_EULER",
    steps=50,
    seed=0,
    safety_check=False,
    output_image_format="JPG",
    init_image_mode="IMAGE_STRENGTH",
)

if answer.image is None:
  raise RuntimeError(f"No return image, {answer.finish_reason}")
else:
  answer.image.save("output_with_bear.jpg")
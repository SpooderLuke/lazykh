import argparse
import torch
from PIL import Image
print(torch.cuda.is_available())
from diffusers import StableDiffusionPipeline
pipe = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4", torch_dtype=torch.float16)
pipe = pipe.to("cuda")
prompt = "floppy disk"
num_images = 1
images = pipe(prompt) 
images.images[0]
images.images[0].save(f"test.png")
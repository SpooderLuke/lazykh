import torch
from diffusers import StableDiffusionPipeline
pipe = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4", torch_dtype=torch.float16)
pipe = pipe.to("cuda")
prompt = "nice cars on speed"
num_images = 1
images = pipe(prompt) 
images.images[0]
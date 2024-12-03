from diffusers import DiffusionPipeline
from diffusers.utils import load_image
from diffusers import FluxPriorReduxPipeline, FluxPipeline
import torch

image = load_image(
    "https://huggingface.co/datasets/YiYiXu/testing-images/resolve/main/style_ziggy/img5.png"
)
device = "cuda"
# Load the FLUX.1 Redux prior pipeline
pipe_prior_redux = FluxPriorReduxPipeline.from_pretrained(
    "black-forest-labs/FLUX.1-Redux-dev", torch_dtype=torch.bfloat16
).to("cuda")

# Load the FLUX.1 base pipeline
pipe = FluxPipeline.from_pretrained(
    "black-forest-labs/FLUX.1-dev",
    text_encoder=None,
    text_encoder_2=None,
    torch_dtype=torch.bfloat16
).to("cuda")

# Generate the prior output
pipe_prior_output = pipe_prior_redux(image)

# Generate the final image
images = pipe(
    guidance_scale=2.5,
    num_inference_steps=50,
    generator=torch.Generator("cpu").manual_seed(0),
    **pipe_prior_output,
).images

# Save the generated image
images[0].save("flux-dev-redux.png")
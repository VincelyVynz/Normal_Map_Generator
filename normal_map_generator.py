import os
import numpy as np
from PIL import Image

input_folder = input("Enter the folder path: ")
output_folder = "output_images"
os.makedirs(output_folder, exist_ok=True)

valid_extensions = ["jpg", "jpeg", "png", "tif", "tiff","targa"]
image_files = [f for f in os.listdir(input_folder) if f.lower().endswith(valid_extensions)]

print(f"{len(image_files)} images found")

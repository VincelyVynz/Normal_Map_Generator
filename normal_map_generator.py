import os
import numpy as np
from PIL import Image

input_folder = input("Enter the folder path: ")
output_folder = "output_images"
os.makedirs(output_folder, exist_ok=True)

valid_extensions = ["jpg", "jpeg", "png", "tif", "tiff","targa"]
image_files = [f for f in os.listdir(input_folder) if f.lower().endswith(valid_extensions)]

print(f"{len(image_files)} images found")

img_dict = {}
for img_name in image_files:
    img_path = os.path.join(input_folder, img_name)
    img=Image.open(img_path).convert("L")
    img_array = np.array(img)

    img_dict[img_name] = img_array
    print(f"Loaded {img_name} with size {img_array.shape}")


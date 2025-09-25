import os
import numpy as np
from PIL import Image

input_folder = input("Enter the folder path: ")
output_folder = "output_images"
os.makedirs(output_folder, exist_ok=True)

valid_extensions = ("jpg", "jpeg", "png", "tif", "tiff","targa")
image_files = [f for f in os.listdir(input_folder) if f.lower().endswith(valid_extensions)]

print(f"{len(image_files)} images found")

img_dict = {}
for img_name in image_files:
    img_path = os.path.join(input_folder, img_name)
    img=Image.open(img_path).convert("L")
    img_array = np.array(img)

    img_dict[img_name] = img_array
    print(f"Loaded {img_name} with size {img_array.shape}")

#Split grayscale image to Tiles

def get_tiles(img_array, tile_size=100):
    """
    Returns a list of tiles with their coordinates.
    Each tile is a tuple: (x_start, y_start, tile_array)
    """
    tiles = []
    height, width = img_array.shape

    for y in range(0, height, tile_size):
        for x in range(0, width, tile_size):
            # Handle tiles at the edges
            tile = img_array[y:min(y + tile_size, height), x:min(x + tile_size, width)]
            tiles.append((x, y, tile))

    return tiles



def tiles_to_normal(tile):
    """
    Converts a grayscale tile to a normal map tile.
    Returns a NumPy array of shape (height, width, 3), dtype=np.uint8
    """
    tile = tile.astype("float")

    dy,dx = np.gradient(tile)
    dz=np.ones_like(tile)

    normal = np.dstack((dx,dy,dz))

    length = np.sqrt(np.sum(normal ** 2, axis=2))
    normal[:,:,0]/=length
    normal[:,:,1]/=length
    normal[:,:,2]/=length

    normal_image = ((normal + 1) * 0.5*255).astype(np.uint8)
    return normal_image











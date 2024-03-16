from PIL import Image
import numpy as np

image = Image.open('imag.png')
image = image.convert('L')
image_array = np.array(image)

np.set_printoptions(threshold=np.inf)

print("Array: ", image_array)

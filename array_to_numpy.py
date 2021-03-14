import numpy as np
from PIL import Image

data = np.zeros((5, 4, 3), dtype=np.uint8)
data[:] = [255, 255, 255]
print(data)

data[1:2, 2:3] = [55, 30, 180]

print(data)

img = Image.fromarray(data, 'RGB')
img.save('canvas.png')

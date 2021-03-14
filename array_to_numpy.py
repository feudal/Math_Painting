import numpy as np
from PIL import Image

data = np.zeros((5, 4, 3), dtype=np.uint8)
data[:] = [255, 255, 0]
print(data)

data[0:3, 0:2] = [55, 30, 180]
data[2:4, 1:3] = [155, 130, 10]

print(data)

img = Image.fromarray(data, 'RGB')
img.save('canvas.png')

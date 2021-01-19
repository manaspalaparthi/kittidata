import scipy
from skimage import color
import numpy as np
from pypardiso import spsolve
from PIL import Image
import matplotlib.pyplot as plt
import imageio



depth_path = "gt.png"
#Load image, convert to numpy array and divide by 256

#image = np.asarray(Image.open(image_path)) /255
depth = np.asarray(Image.open(depth_path))


#depth = imageio.imread(depth_path)
#print(depth[:100 , :100 ])


plt.figure(figsize=(10, 10))
plt.imshow(depth[ : : 0])
plt.title("Ground Truth", fontsize=22)
plt.show()
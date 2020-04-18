import cv2
import numpy as np
import matplotlib
from matplotlib import pyplot as plt
from numpy.fft import fftshift, ifftshift, fftn, ifftn

matplotlib.rcParams['font.size'] = 8.0
np.random.seed(19680801)

img = cv2.imread('p2.jpg', 0)
dim = range(img.ndim)

k = fftshift(fftn(ifftshift(img, axes=dim), s=None, axes=dim), axes=dim)
k /= np.sqrt(np.prod(np.take(img.shape, dim)))
k = np.real(k)
magnitude_spectrum = 20 * np.log(np.abs(k) + 1)

images = []

fig, axs = plt.subplots(1, 2)

for j in range(2):
    axs[j].set_yticklabels([])
    axs[j].set_xticklabels([])

data = [img, magnitude_spectrum]

images.append(axs[0].imshow(data[0], cmap='gray'))
axs[0].set_title('Input Image')

images.append(axs[1].imshow(data[1], cmap='gray'))
axs[1].set_title('K-space')

plt.show()
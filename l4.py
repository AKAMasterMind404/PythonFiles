# %%
"""
# Tc6
# LAB 04
"""

# %%
"""
## `NAME`: Atharv Karbhari
## `PRN`: 20190802003
"""

# %%
"""
### `AIM`: To study and perform low-level feature extraction on image data.
"""

# %%
"""
### `To Perform`:
A. Edge Detection using Prewitt filter.

B. Canny edge detection.

C. Laplacian of Gaussian

D. Perform and comparison between Gradient-based and Gaussian-based operators
"""

# %%
"""
**Importing necessary libraries**
"""

# %%
import matplotlib.pyplot as plt
import numpy as np
from skimage.io import imread, imshow
from skimage.filters import apply_hysteresis_threshold, sobel, sobel_v, sobel_h, unsharp_mask, gaussian, prewitt, prewitt_h, prewitt_v
from skimage.color import rgb2gray, rgba2rgb
from skimage.feature import blob_log

import cv2

# %%
"""
**Import and read the image**
"""

# %%
color = imread('veg.png')
gray = rgb2gray(rgba2rgb(color))

# %%
"""
**A. Edge Detection using Prewitt filter**
"""

# %%
mask = unsharp_mask(gray, radius=5, amount=2.0)
fig, ax = plt.subplots(3, 2)
fig.set_size_inches(15, 15)
imshow(gray, ax=ax[0, 0])
imshow(mask, ax=ax[0, 1])

h_gray_prewitt = prewitt_h(gray, mask)
imshow(h_gray_prewitt, ax=ax[1, 0], cmap="gray")
v_gray_prewitt = prewitt_v(gray, mask)
imshow(v_gray_prewitt, ax=ax[1, 1], cmap='gray')
gray_prewitt = prewitt(gray, mask)
imshow(gray_prewitt, ax=ax[2, 0], cmap='gray')

# %%
"""
**B. Canny edge detection**
"""

# %%
gray_gaussian = gaussian(gray)
fig2, ax2 = plt.subplots(3, 2)
fig2.set_size_inches(15, 15)
imshow(gray, ax=ax2[0, 0])
imshow(gray_gaussian, ax=ax2[0, 1])
edge_sobel_v = sobel_v(gray_gaussian)
imshow(edge_sobel_v, cmap='gray', ax=ax2[1, 0])
edge_sobel_h = sobel_h(gray_gaussian)
imshow(edge_sobel_h, cmap='gray', ax=ax2[1, 1])
edge_sobel = sobel(gray)
imshow(edge_sobel, cmap='gray', ax=ax2[2, 0])
edge_sobel_hysteresis = apply_hysteresis_threshold(edge_sobel, 0.5, 1.5)

imshow(edge_sobel_hysteresis, ax=ax2[2, 1])

# %%
"""
**C. Laplacian of Gaussian**
"""

# %%
gray_gaussian = gaussian(gray)  # Applying Gaussian filter
gray_log = cv2.Laplacian(gray_gaussian, cv2.CV_64F)  # Applying log filter

img, ax3 = plt.subplots(2, 2)
img.set_size_inches(15, 15)

ax3[0, 0].title.set_text("original")
imshow(gray, ax=ax3[0, 0], cmap='gray')

ax3[0, 1].title.set_text("Gaussian")
imshow(gray_gaussian, ax=ax3[0, 1])

ax3[1, 0].title.set_text("Log filter")
imshow(gray_log, ax=ax3[1, 0], cmap='gray')

ax3[1, 1].title.set_text("Log Output Image")
imshow(gray + gray_log, ax=ax3[1, 1], cmap='gray')

# %%
"""
### `CONCLUSION`: Hence we have succesfully studied and performed low-level feature extraction on image data.
"""

# %%

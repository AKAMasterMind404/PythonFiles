# %%
"""
## `NAME`: Atharv Karbhari
## `PRN`: 20190802003
"""

# %%
"""
### `AIM`: To perform transformation and filtering on the image.
"""

# %%
"""
**Importing required libraries**
"""

# %%
import numpy as np
import cv2
from matplotlib import pyplot as plt
# from skimage.color import rgb2hsv, rgb2gray, rgb2yuv
from PIL import Image

# %%
"""
## `A. IMAGE TRANSFORMATION`
"""

# %%
img = cv2.imread('veg.png', 0)

# %%
img

# %%
plt.imshow(img)

# %%
dark_image_grey_fourier = np.fft.fftshift(np.fft.fft2(img))
plt.figure(num=None, figsize=(8, 6), dpi=80)
plt.imshow(np.log(abs(dark_image_grey_fourier)), cmap='gray');

# %%
grayscale = cv2.cvtColor(img, cv2.IMREAD_GRAYSCALE)

# %%
plt.imshow(grayscale)

# %%
plt.subplot(121), plt.imshow(img, cmap='gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.show()


# %%
def fourier_transform_rgb(image):
    f_size = 25
    transformed_channels = []
    for i in range(3):
        rgb_fft = np.fft.fftshift(np.fft.fft2((image[:, :, i])))
        rgb_fft[:225, 235:237] = 1
        rgb_fft[-225:, 235:237] = 1
        transformed_channels.append(abs(np.fft.ifft2(rgb_fft)))

    final_image = np.dstack([transformed_channels[0].astype(int),
                             transformed_channels[1].astype(int),
                             transformed_channels[2].astype(int)])

    fig, ax = plt.subplots(1, 2, figsize=(17, 12))
    ax[0].imshow(image)
    ax[0].set_title('Original Image', fontsize=f_size)
    ax[0].set_axis_off()

    ax[1].imshow(final_image)
    ax[1].set_title('Transformed Image', fontsize=f_size)
    ax[1].set_axis_off()

    fig.tight_layout()


# %%
fourier_transform_rgb(grayscale)

# %%
"""
## `B. PERFORM FOLLOWING OPERATION`
"""

# %%
"""
**1. Smoothing and weigthed average**
"""

# %%
image = cv2.imread('veg.png', 0)

kernel2 = np.ones((5, 5))
img = cv2.filter2D(src=image, ddepth=-1, kernel=kernel2)

# %%
plt.imshow(image)

# %%
plt.imshow(img)

# %%
"""
**2. Median Filter**
"""


# %%
def median_filter(data, kernel_size):
    temp = []
    indexer = kernel_size // 2
    data_final = []
    data_final = np.zeros((len(data), len(data[0])))
    for i in range(len(data)):

        for j in range(len(data[0])):

            for z in range(kernel_size):
                if i + z - indexer < 0 or i + z - indexer > len(data) - 1:
                    for c in range(kernel_size):
                        temp.append(0)
                else:
                    if j + z - indexer < 0 or j + indexer > len(data[0]) - 1:
                        temp.append(0)
                    else:
                        for k in range(kernel_size):
                            temp.append(data[i + z - indexer][j + k - indexer])

            temp.sort()
            data_final[i][j] = temp[len(temp) // 2]
            temp = []
    return data_final


def rgb2gray(rgb):
    return np.dot(rgb[..., :3], [0.2989, 0.5870, 0.1140])


# %%
img = rgb2gray(plt.imread("veg.png"))

# %%
removed_noise_3 = median_filter(img, 3)
plt.subplot(121), plt.imshow(img), plt.title('median_filter')
plt.show()

# %%
"""
**3. Laplacian filter**
"""

# %%
ddepth = cv2.CV_16S
kernel_size = 3
window_name = "Laplace Demo"

src = cv2.imread(cv2.samples.findFile("veg.png"), cv2.IMREAD_COLOR)

if src is None:
    print('Error opening image')
    print('Program Arguments: [image_name -- default lena.jpg]')

src = cv2.GaussianBlur(src, (3, 3), 0)
src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
cv2.namedWindow(window_name, cv2.WINDOW_AUTOSIZE)
dst = cv2.Laplacian(src_gray, ddepth, ksize=kernel_size)
abs_dst = cv2.convertScaleAbs(dst)

plt.imshow(abs_dst)

# %%
"""
**4. Composite masking filter**
"""

# %%
image = Image.open(r"veg.png").convert('L')

# %%
image_composite = Image.composite(image, image, image)

# %%
plt.imshow(image_composite)

# %%
"""
**5. High boost filter**
"""


# %%
def highBoostFiltering(image, boost_factor):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Converting Image to Gray Scale
    resultant_image = image.copy()
    for i in range(1, image.shape[0] - 1):
        for j in range(1, image.shape[1] - 1):
            blur_factor = (image[i - 1, j - 1] + image[i - 1, j] - image[i - 1, j + 1] + image[i, j - 1] + image[i, j] +
                           image[i, j + 1] + image[i + 1, j + 1] + image[i + 1, j] + image[i + 1, j + 1]) / 9
            mask = boost_factor * image[i, j] - blur_factor
            resultant_image[i, j] = image[i, j] + mask

    return resultant_image


# %%
img = cv2.imread('veg.png')
output = highBoostFiltering(img, 5)

# %%
plt.imshow(output)

# %%
"""
**6. Shobel filter**
"""

# %%
cap = cv2.imread("veg.png")

sobelx = cv2.Sobel(cap, cv2.CV_64F, 1, 0, ksize=5)
sobely = cv2.Sobel(cap, cv2.CV_64F, 0, 1, ksize=5)

# %%
plt.imshow(sobelx)

# %%
plt.imshow(sobely)

# %%
"""
### `CONCLUSION`: Hence we have succesfully implemented the image transformation with different methods in python
"""

# %%

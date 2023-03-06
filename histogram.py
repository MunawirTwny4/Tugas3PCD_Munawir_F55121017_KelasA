import cv2
import numpy as np
import matplotlib.pyplot as plt

def calculate_histogram(image):
    histogram = np.zeros((256,))
    for pixel_value in range(256):
        histogram[pixel_value] = np.sum(image == pixel_value)
    return histogram

image = cv2.imread("Gambar Histogram.jpg", cv2.IMREAD_GRAYSCALE)

histogram = calculate_histogram(image)

plt.plot(histogram)
plt.title("Histogram")
plt.xlabel("Pixel Value")
plt.ylabel("Frequency")
plt.show()

cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
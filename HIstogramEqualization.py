import cv2
import numpy as np
import matplotlib.pyplot as plt

def calculate_histogram(image):
    histogram = np.zeros((256,))
    for pixel_value in range(256):
        histogram[pixel_value] = np.sum(image == pixel_value)
    return histogram

def histogram_equalization(image):
    histogram = calculate_histogram(image)

    cumulative_histogram = np.cumsum(histogram)

    normalized_histogram = (cumulative_histogram - cumulative_histogram.min()) * 255 / (
                cumulative_histogram.max() - cumulative_histogram.min())
    normalized_histogram = normalized_histogram.astype('uint8')

    equalized_image = normalized_histogram[image]

    return equalized_image

image = cv2.imread("Gambar HistogramEquali.jpg", cv2.IMREAD_GRAYSCALE)

equalized_image = histogram_equalization(image)

cv2.imshow("Original Image", image)
cv2.imshow("Equalized Image", equalized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

histogram = calculate_histogram(image)
plt.plot(histogram)
plt.title("Original Histogram")
plt.xlabel("Pixel Value")
plt.ylabel("Frequency")
plt.show()

histogram_equalized = calculate_histogram(equalized_image)
plt.plot(histogram_equalized)
plt.title("Equalized Histogram")
plt.xlabel("Pixel Value")
plt.ylabel("Frequency")
plt.show()
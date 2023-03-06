import numpy as np
import cv2

def average_filter(image, kernel_size):
    padding_size = kernel_size // 2
    padded_image = cv2.copyMakeBorder(image, padding_size, padding_size, padding_size, padding_size, cv2.BORDER_REPLICATE)

    height, width = image.shape[:2]
    kernel = np.ones((kernel_size, kernel_size), np.float32) / (kernel_size ** 2)

    filtered_image = np.zeros((height, width), np.uint8)
    for i in range(padding_size, height + padding_size):
        for j in range(padding_size, width + padding_size):
            roi = padded_image[i - padding_size:i + padding_size + 1, j - padding_size:j + padding_size + 1]
            filtered_image[i - padding_size, j - padding_size] = np.sum(np.multiply(roi, kernel))

    return filtered_image

image = cv2.imread("Gambar Average.jpg", cv2.IMREAD_GRAYSCALE)
filtered_image = average_filter(image, 3)

cv2.imshow("Original Image", image)
cv2.imshow("Filtered Image", filtered_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
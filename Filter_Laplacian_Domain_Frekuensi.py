import cv2
import numpy as np
import matplotlib.pyplot as plt

def laplacian_frequency(image):
    # Menghitung ukuran citra
    rows, cols = image.shape
    # Mengambil citra frekuensi dengan transformasi Fourier
    f = np.fft.fft2(image)
    # Menghitung filter Laplacian
    h = np.zeros((rows, cols), dtype=np.float32)
    for i in range(rows):
        for j in range(cols):
            h[i, j] = -4 * np.pi ** 2 * (i ** 2 + j ** 2)
    # Mengalikan filter Laplacian dengan citra frekuensi
    filtered_f = h * f
    # Mengambil citra hasil filter dengan transformasi invers Fourier
    filtered_img = np.fft.ifft2(filtered_f)
    # Menormalisasi citra hasil filter
    filtered_img = np.real(filtered_img)
    filtered_img = filtered_img / filtered_img.max()
    return filtered_img

# Membaca citra grayscale
img = cv2.imread('Filter.jpg', cv2.IMREAD_GRAYSCALE)

# Menampilkan citra asli
plt.figure(figsize=(5, 5))
plt.imshow(img, cmap='gray')
plt.title('Citra Asli')
plt.axis('off')

# Menerapkan filter Laplacian di domain frekuensi
filtered_img = laplacian_frequency(img)

# Menampilkan citra hasil filter
plt.figure(figsize=(5, 5))
plt.imshow(filtered_img, cmap='gray')
plt.title('Citra Hasil Filter')
plt.axis('off')
plt.show()

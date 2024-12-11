import imageio.v2 as imageio
import numpy as np
import matplotlib.pyplot as plt

# Membaca gambar
image = imageio.imread('e://Data Alya//Sem 5//PengolahanCitraDigital//singa.jpg', mode='L')

# Operator Robert
def roberts_edge_detection(image):
    kernel_x = np.array([[1, 0], [0, -1]])
    kernel_y = np.array([[0, 1], [-1, 0]])
    
    # Menghitung gradien
    grad_x = np.zeros(image.shape)
    grad_y = np.zeros(image.shape)
    
    for i in range(image.shape[0] - 1):
        for j in range(image.shape[1] - 1):
            grad_x[i, j] = np.sum(kernel_x * image[i:i+2, j:j+2])
            grad_y[i, j] = np.sum(kernel_y * image[i:i+2, j:j+2])
    
    return np.sqrt(grad_x**2 + grad_y**2)

# Operator Sobel
def sobel_edge_detection(image):
    kernel_x = np.array([[1, 0, -1], [2, 0, -2], [1, 0, -1]])
    kernel_y = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])
    
    grad_x = np.zeros(image.shape)
    grad_y = np.zeros(image.shape)
    
    for i in range(1, image.shape[0] - 1):
        for j in range(1, image.shape[1] - 1):
            grad_x[i, j] = np.sum(kernel_x * image[i-1:i+2, j-1:j+2])
            grad_y[i, j] = np.sum(kernel_y * image[i-1:i+2, j-1:j+2])
    
    return np.sqrt(grad_x**2 + grad_y**2)

# Menghitung deteksi tepi
edges_roberts = roberts_edge_detection(image)
edges_sobel = sobel_edge_detection(image)

# Visualisasi hasil
plt.figure(figsize=(12, 6))
plt.subplot(1, 3, 1)
plt.title('Gambar Asli')
plt.imshow(image, cmap='gray')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.title('Deteksi Tepi Robert')
plt.imshow(edges_roberts, cmap='gray')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.title('Deteksi Tepi Sobel')
plt.imshow(edges_sobel, cmap='gray')
plt.axis('off')

plt.show()
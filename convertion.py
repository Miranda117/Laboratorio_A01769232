import numpy as np
from scipy import signal


# Funcion para calcular la convolución de una matriz de dos dimensiones 
def convolution(image, kernel):
    #Se hace uso de el metodo convolve2d que viene de la libreria scipy
    output_matrix = signal.convolve2d(image, kernel, mode="valid")
    print ("this is the final matix")
    print (output_matrix)
    return output_matrix


def request_matrix():
    #El usuario ingresa las los renglones y columnas de la matriz de la imagen
    rowImage = int(input("Enter the number of rows of the image matrix: "))
    colImage = int(input("Enter the number of cols of the image matrix: "))
    image = np.zeros([rowImage, colImage])

    for i in range(0, rowImage, 1):
        for j in range(0, colImage, 1):

            valueMatri = float(input("Enter the value: "))
            image[i, j] = valueMatri
    print ("Original matrix:")
    print(image)
    kernel = request_kernel()
    return image, kernel


def request_kernel():
    #El usuario ingresa las los renglones y columnas de la matriz de la kernel

    row_kernel = int(input("Enter the number of rows of the kernel: "))
    col_kernel = row_kernel
    kernel = np.zeros([row_kernel, col_kernel])

    for i in range(row_kernel):
        for j in range(col_kernel):

            value_kernel = float(input("Enter the value: "))
            kernel[i, j] = value_kernel
    print ("kernel: ")
    print(kernel)
    return kernel

if __name__ == "__main__":
    image, kernel = request_matrix()
    convoli = convolution(image, kernel) #Resibe los parametros de la matiz de imagen y kernel

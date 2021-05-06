import numpy as np


def conv_helper(fragment, kernel):
    f_row, f_col = fragment.shape
    k_row, k_col = kernel.shape
    result = 0.0
    for row in range(f_row):
        for col in range(f_col):
            result += fragment[row, col] * kernel[row, col]
    return result


def convolution(image, kernel):

    image_row, image_col = image.shape
    kernel_row, kernel_col = kernel.shape
    output = np.zeros(image.shape)

    for row in range(image_row):
        for col in range(image_col):
                output[row, col] = conv_helper(
                        image[row:row + kernel_row,
                        col:col + kernel_col], kernel)

    print (output)
    return output


if __name__ == "__main__":
    rowImage = int(input("Enter the number of rows of the image matrix: "))
    colImage = int(input("Enter the number of cols of the image matrix: "))
    image = np.zeros([rowImage, colImage])
    kernel = np.array([[1, 1, 1], [0, 0, 0], [2, 10, 3]])
    for i in range(0, rowImage, 1):
        for j in range(0, colImage, 1):

            valueMatri = int(input("Enter the value: "))
            image[i, j] = valueMatri
    print ("Matriz :")
    print(image)

    convoli = convolution(image, kernel)

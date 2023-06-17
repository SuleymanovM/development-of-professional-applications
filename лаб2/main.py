import numpy as np

def generate_matrix(n):
    """
    Генерация квадратной матрицы размера n x n со случайными целочисленными значениями от 0 до 9
    """
    return np.random.randint(10, size=(n, n))

def sum_diagonal_parallel(matrix):
    """
    Вычисление суммы элементов, расположенных параллельно главной диагонали (ближайшие к главной)
    """
    diagonal_sum = 0
    for i in range(1, len(matrix)):
        # Суммируем элементы выше главной диагонали
        diagonal_sum += np.sum(np.diagonal(matrix, offset=i))
        # Суммируем элементы ниже главной диагонали
        diagonal_sum += np.sum(np.diagonal(matrix, offset=-i))
    # Суммируем элементы на главной диагонали
    diagonal_sum += np.sum(np.diagonal(matrix))
    return diagonal_sum

def save_to_file(filename, matrix, diagonal_sum):
    """
    Сохранение исходных данных и результата обработки в файл
    """
    with open(filename, 'w') as f:
        f.write("Matrix:\n")
        np.savetxt(f, matrix, fmt="%d")
        f.write("\n\nOriginal Matrix:\n")
        np.savetxt(f, matrix, fmt="%d")
        f.write("\nSum of elements parallel to the main diagonal: ")
        f.write(str(diagonal_sum))

# Задаем размер квадратной матрицы
n = 5

# Генерируем матрицу
matrix = generate_matrix(n)

# Вычисляем сумму элементов, расположенных параллельно главной диагонали
diagonal_sum = sum_diagonal_parallel(matrix)

# Сохраняем исходные данные и результат обработки в файл
filename = "result.txt"
save_to_file(filename, matrix, diagonal_sum)

# Выводим исходные данные и результат обработки в консоль
with open(filename, 'r') as f:
    print(f.read())

# Выводим исходные данные и результат обработки в консоль
print("Matrix:")
print(matrix)
print("\nSum of elements parallel to the main diagonal:", diagonal_sum)
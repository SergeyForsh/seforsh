# Функции в Python. Функция с параметром
print('Функции в Python.Функция с параметром')
print()
def get_matrix (n,m, value):
    matrix = []
    if n <= 0 or m <=0:
        return matrix
    for i in range (n):
        matrix.append([])
        for j in range (m):
            matrix [i].append(value)
    return matrix
result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
result4 = get_matrix(5, 0, 0)
print(result1)
print(result2)
print(result3)
print(result4)
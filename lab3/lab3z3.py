import numpy as np
from scipy.optimize import linprog

# Об'єктивна функція для двоїстої задачі
c_dual = [50, -16, 12, 25, 30]

# Матриця коефіцієнтів обмежень для двоїстої задачі
A_dual = [
    [-6, -9, -4, -9, 2],   # нерівність для y1
    [-4, -7, 2, 2, -3]     # нерівність для y2
]

# Вектор правої частини обмежень для двоїстої задачі
b_dual = [2, -6]

# Розв'язок двоїстої задачі
result_dual = linprog(c_dual, A_ub=A_dual, b_ub=b_dual, method='simplex')

# Вивід результатів
print('Optimal values for dual problem:')
print('y1 =', result_dual.x[0])
print('y2 =', result_dual.x[1])
print('y3 =', result_dual.x[2])
print('y4 =', result_dual.x[3])
print('y5 =', result_dual.x[4])
print('Optimal objective function value for dual problem:', result_dual.fun)

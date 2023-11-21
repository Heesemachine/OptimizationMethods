import numpy as np
from scipy.optimize import linprog
from pulp import LpMaximize, LpProblem, LpVariable, lpSum

# Об'єктивна функція для максимізації
c = [-2, 6]

# Матриця коефіцієнтів обмежень
A = [[6, 4], [-9, -7], [4, -2], [9, -2], [-2, 3]]

# Вектор правої частини обмежень
b = [50, -16, 12, 25, 30]

# Розв'язок задачі ЛП з використанням методу штучних змінних
result = linprog(c, A_ub=A, b_ub=b, method='simplex')

# Вивід результатів
print('Optimal values:')
print('x1 =', result.x[0])
print('x2 =', result.x[1])
print('Optimal objective function value:', -result.fun)

# Задача цілочисельного програмування з використанням PuLP
x1 = LpVariable("x1", lowBound=0, cat="Integer")
x2 = LpVariable("x2", lowBound=0, cat="Integer")

# Об'єктивна функція
objective = c[0] * x1 + c[1] * x2

# Задача
problem = LpProblem(name="IntegerProgramming", sense=LpMaximize)
problem += objective

# Обмеження
for i in range(len(A)):
    problem += lpSum(A[i][j] * [x1, x2][j] for j in range(len(c))) <= b[i]

# Розв'язок
problem.solve()

# Вивід результатів цілочисельного програмування
print('\nInteger Programming Solution:')
print('x1 =', int(x1.value()))
print('x2 =', int(x2.value()))
print('Optimal objective function value:', int(objective.value()))

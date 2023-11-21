import numpy as np
from scipy.optimize import linprog
import matplotlib.pyplot as plt

# Об'єктивна функція для максимізації
c = [-2, 6]

# Матриця коефіцієнтів обмежень
A = [[6, 4], [-9, -7], [-4, 2], [9, -2], [2, -3]]

# Вектор правої частини обмежень
b = [50, -16, -12, 25, -30]

# Діапазон значень x1 і x2 для графіку
x1_range = np.linspace(0, 10, 400)
x2_range = np.linspace(0, 10, 400)

# Створення координатної сітки
X1, X2 = np.meshgrid(x1_range, x2_range)

# Обчислення значень лівої частини кожного обмеження для графіку
ineq1 = 6*X1 + 4*X2 - 50 <= 0
ineq2 = -9*X1 - 7*X2 + 16 <= 0
ineq3 = -4*X1 + 2*X2 - 12 <= 0
ineq4 = 9*X1 - 2*X2 - 25 <= 0
ineq5 = 2*X1 - 3*X2 + 30 <= 0

# Побудова графіку
plt.figure(figsize=(8, 8))

# Відображення ліній обмежень
plt.plot(x1_range, (50 - 6*x1_range) / 4, label=r'$6x_1 + 4x_2 \leq 50$')
plt.plot(x1_range, (16 + 9*x1_range) / 7, label=r'$9x_1 + 7x_2 \geq 16$')
plt.plot(x1_range, (12 + 4*x1_range) / 2, label=r'$4x_1 - 2x_2 \geq 12$')
plt.plot(x1_range, (25 - 9*x1_range) / -2, label=r'$9x_1 - 2x_2 \leq 25$')
plt.plot(x1_range, (30 + 2*x1_range) / 3, label=r'$-2x_1 + 3x_2 \leq 30$')

# Заповнення області
plt.fill_between(x1_range, 0, np.minimum.reduce([50 - 6*x1_range, (16 + 9*x1_range) / 7, (12 + 4*x1_range) / 2, 25 - 9*x1_range / -2, (30 + 2*x1_range) / 3]), color='gray', alpha=0.5)

plt.xlabel('x1')
plt.ylabel('x2')
plt.title('Feasible Region')
plt.legend()
plt.grid(True)
plt.show()

# Розв'язок задачі ЛП
result = linprog(c, A_ub=A, b_ub=b, method='highs')

# Перевірка чи був знайдений розв'язок
if result.success:
    # Вивід результатів
    print('Optimal values:')
    print('x1 =', result.x[0])
    print('x2 =', result.x[1])
    print('Optimal objective function value:', -result.fun)
else:
    print('Optimization failed. No solution found.')

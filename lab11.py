import numpy as np
import matplotlib.pyplot as plt

# Define the function f(x)
def f(x):
    return (x ** 10 / 5) - (50 - np.abs(x)) ** (3/2)

# Define the first derivative of f(x)
def f_derivative(x):
    if x == 0:
        return None
    elif x > 0:
        return (10/5) * x ** 2 + (3/2) * np.sqrt(50 - x)
    else:
        return (10/5) * x ** 2 - (3/2) * np.sqrt(50 + x)

# Define the second derivative of f(x)
def f_second_derivative(x):
    if x == 0:
        return None
    elif x > 0:
        return (10/5) * x + (3 / (4 * np.sqrt(50 - x)))
    else:
        return (10/5) * x - (3 / (4 * np.sqrt(50 + x)))

# Number of data points for plotting
n = 1000
x = np.linspace(-10, 10, n)
y = np.array([f(e) for e in x])
y_derivative = np.array([f_derivative(e) for e in x])

# Create subplots for the function and its derivative
fig, ax = plt.subplots(1, 2, figsize=(8, 4))
ax[0].plot(x, y, c='k')
ax[0].set_title("Function f(x)")
ax[0].grid()

ax[1].plot(x[:500:], y_derivative[:500:], c='k')
ax[1].plot(x[501::], y_derivative[501::], c='k')
ax[1].set_title("Derivative f(x)")
ax[1].grid()

plt.show()

# Dichotomy
e = 0.01

a = -6
b = 5

while np.abs(b - a) > 2*e:
    x = (a + b) / 2
    x1 = (a + b - e) / 2
    x2 = (a + b + e) / 2
    
    if f(x1) > f(x2):  # f(x1) > f(x2) for maximum / f(x1) < f(x2) for minimum
        b = x2
    else:
        a = x1
else:
    print(f"Lcal maximum {f(x):.2f} at x {x:.2f}")
# Golden Section Search
e = 0.01

a = -6
b = 5

phi = (1 + np.sqrt(5)) / 2

while np.abs(b - a) > 2*e:
    x = (a + b) / 2
    x1 = b - (b-a) / phi
    x2 = a + (b-a) / phi
    
    if f(x1) > f(x2):  # f(x1) > f(x2) for a maximum, f(x1) < f(x2) for a minimum
        b = x2
    else:
        a = x1
else:
    print(f"Local maximum {f(x):.2f} at x = {x:.2f}")

# Newton's Method
e = 0.001

x0 = 0.5
x1 = x0 - (f_derivative(x0) / f_second_derivative(x0))

while np.abs(x1 - x0) > 2*e:
    x0 = x1
    x1 = x1 - (f_derivative(x1) / f_second_derivative(x1))
else:
    print(f"Local maximum {f(x):.2f} at x = {x:.2f}")

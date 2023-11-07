import sympy as sp

# Calculate k
k = 10 - round(10 / 6) * 6

# Define symbolic variables for x, y, and z
x, y, z = sp.symbols('x y z')

# Define the given values
v = 3  # You didn't provide a value for v, so I'm assuming it's 3

# Define the equations
eq1 = 15 * x + (v / 3) * y + (5 + k) * z
eq2_positive_x = (k + 1) * x + y**2 - (10 + 7)
eq2_negative_x = (k + 1) * (-x) + y**2 - (10 + 7)
eq3 = x**2 + y**2 - (10 + 4)**2

# Solve the system of equations for positive x
solutions_positive_x = sp.solve((eq1, eq2_positive_x, eq3), (x, y, z))

# Solve the system of equations for negative x
solutions_negative_x = sp.solve((eq1, eq2_negative_x, eq3), (x, y, z))

# Combine the solutions
solutions = solutions_positive_x + solutions_negative_x

# Print the solutions
for solution in solutions:
    x_value, y_value, z_value = solution
    print(f"x = {x_value}, y = {y_value}, z = {z_value}")

# Calculate k and the other values
print(f"k = {k}")

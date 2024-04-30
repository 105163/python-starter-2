from math import sqrt, factorial

def calc_e():
    # Calculate e using the series expansion
    e = 0
    for i in range(20):  # Increase number of terms for better precision
        e += 1 / factorial(i)
    return e

def solve_equation(a, b, c):
    if a == 0 and b == 0:
        raise ValueError("a and b cannot both be zero")
    if a == 0:  # Linear case: bx + c = 0
        return ((-c / b), None)
    
    # Compute discriminant
    D = b**2 - 4*a*c
    if D < 0:
        return (None, None)  # No real solutions
    elif D == 0:
        x = -b / (2 * a)
        return (x, None)  # One real solution
    else:
        sqrt_D = sqrt(D)
        x1 = (-b + sqrt_D) / (2 * a)
        x2 = (-b - sqrt_D) / (2 * a)
        return (min(x1, x2), max(x1, x2))  # Two real solutions

if __name__ == "__main__":
    print("Calculated e:", calc_e())
    print("Solutions for x^2 + 3x + 2 = 0:", solve_equation(1, 3, 2))
    print("Solutions for x^2 + x + 1 = 0:", solve_equation(1, 1, 1))

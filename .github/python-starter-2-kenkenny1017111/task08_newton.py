def fixed_point_iteration(g, x0, n):
    results = [x0]
    x = x0
    for _ in range(n):
        x = g(x)
        results.append(x)
    return results

def newton(f, fp, x0, eps=1e-7, n=100000):
    x = x0
    for _ in range(n):
        fx = f(x)
        fpx = fp(x)
        if abs(fpx) < eps:
            return None  # Avoid division by zero
        x_new = x - fx / fpx
        if abs(x_new - x) < eps:
            return x_new
        x = x_new
    return None

if __name__ == "__main__":
    def g(x):
        return (x * x + 1) / 3

    print(fixed_point_iteration(g, 1.0, 2))

    def f0(x):
        return x * x - 5

    def f1(x):
        return 2 * x

    x0 = 2.0
    solution = newton(f0, f1, x0)
    print(solution)

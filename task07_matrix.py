import numpy as np

def is_square(m):
    return m.shape[0] == m.shape[1]

def is_symmetric(m):
    if not is_square(m):
        return False
    return np.array_equal(m, m.T)

def is_skew_symmetric(m):
    if not is_square(m):
        return False
    return np.array_equal(m, -m.T)

def is_upper_triangular(m):
    if not is_square(m):
        return False
    return np.allclose(m, np.triu(m))

def is_lower_triangular(m):
    if not is_square(m):
        return False
    return np.allclose(m, np.tril(m))

def is_diagonal(m):
    if not is_square(m):
        return False
    return np.allclose(m, np.diag(np.diag(m)))

def classify_linear_system(aug):
    # Simplified classification using rank comparison
    rows, cols = aug.shape
    if cols - 1 > rows:
        return "none"
    rank_full = np.linalg.matrix_rank(aug)
    rank_coeff = np.linalg.matrix_rank(aug[:, :-1])
    if rank_full != rank_coeff:
        return "none"
    elif rank_full == cols - 1:
        return "unique"
    else:
        return "many"

if __name__ == "__main__":
    matrix = np.array([[1, 2], [3, 4]])
    print("Square:", is_square(matrix))
    print("Symmetric:", is_symmetric(matrix))
    print("Skew Symmetric:", is_skew_symmetric(matrix))
    print("Upper Triangular:", is_upper_triangular(matrix))
    print("Lower Triangular:", is_lower_triangular(matrix))
    print("Diagonal:", is_diagonal(matrix))

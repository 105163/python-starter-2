import math
import numpy as np

def rotation_matrix_2d(theta):
    c, s = np.cos(theta), np.sin(theta)
    return np.array([[c, -s], [s, c]])

def rotation_matrix_2d_degree(deg):
    theta = np.deg2rad(deg)
    return rotation_matrix_2d(theta)

def distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def rotate(p, theta):
    rm = rotation_matrix_2d(theta)
    rotated_p = np.dot(rm, np.array(p))
    # Round small values to zero
    rotated_p = np.round(rotated_p, decimals=10)  # Adjust decimals as needed
    return tuple(rotated_p)

if __name__ == "__main__":
    print('2D Rotation Matrix for PI radians:', rotation_matrix_2d(math.pi))
    print('2D Rotation Matrix for 180 degrees:', rotation_matrix_2d_degree(180))
    p1 = (7, 3)
    p2 = (3, 0)
    d = distance(p1, p2)
    print('Distance between points:', d)  # should give 5
    p2_new = rotate(p2, math.pi / 2)  # should give (0, 3)
    print('Point after rotation:', p2_new)

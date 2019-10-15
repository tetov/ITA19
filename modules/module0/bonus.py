""" Assignment for module1 in ITA19 COMPAS course
"""

__author__ = "Anton T Johansson"

import random
from typing import List
import pdb 


def mul_matrix(matrix: List[float], multiplier: float) -> List[float]:
    return [i * multiplier for i in matrix]


def vector_on_plane(point: List[float],
                         normal: List[float]) -> List[float]:
    '''
    '''
    # plane equation
    # Ax + By + Cz = D

    # std equation plane (abc is normal, xyz1 is given point, xyz is vector)
    # a(x-x1) + b(y-y1) + c(z-z1) = 0

    # isolate one vector component
    # x = ( -b(y-y1) -c(z-z1) / a +x1

    a, b, c = normal
    x1, y1, z1 = point
    y, z = random.random(), random.random()

    x = (-b * (y - y1) - c * (z - z1)) / a + x1

    # https://www.youtube.com/watch?v=p_JItfXpGlQ

    return [x, y, z] 


if __name__ == "__main__":

    print("Module0 bonus, by " + __author__ + "\n")
    print(
        "Returns vector that rests within plane defined by point on plane and plane's normal...\n"
    )

    input_point = input("Enter a point, three values separated by comma: ")
    input_normal = input(
        "Enter the normal vector, three values separated by comma: ")

    point = list(map(float, input_point.split(",")))
    normal = list(map(float, input_normal.split(",")))

    perp_vector = vector_on_plane(point, normal)

    pdb.set_trace()


    print("The vector ({}, {}, {}) rests within given plane".format(
        *perp_vector))

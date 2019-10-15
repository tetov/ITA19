""" Assignment for module1 in ITA19 COMPAS course
"""

__author__ = "Anton T Johansson"

import ast
from math import radians
from pathlib import Path
from typing import List, Tuple

from compas.geometry import Vector, dot_vectors_xy, rotate_points_xy


def is_cww(pt_A: Tuple[float], pt_B: Tuple[float], pt_C: Tuple[float]) -> bool:
    """ Checks if vector AB is oriented clockwise or counter-clockwise to
        vector AC.

        Parameters
        ----------
        pt_a, pt_b, pt_c : list or tuple of floats

        Returns
        -------
        bool

        >>> is_cww((20,30), (40,10), (12,25))
        False
    """
    # create the two vectors, but one is rotated 90 degrees
    # based on https://gamedev.stackexchange.com/questions/45412/
    vector_AC = Vector.from_start_end((*pt_A, 0), (*pt_C, 0))

    rot_B = rotate_points_xy([pt_B], radians(90), pt_A)
    rotated_AB = Vector.from_start_end((*pt_A, 0), *rot_B)

    # positive dot product ccw
    angle_between = dot_vectors_xy(rotated_AB, vector_AC)
    if angle_between > 0:
        return True
    if angle_between < 0:
        return False

    raise ValueError('Vectors have the same direction')


def get_tuple_from_file(path: Path) -> List[Tuple[float]]:
    """ Read file and store lines as tuple.
        File needs to be formatted in python syntax
    """
    tuples_of_pts = []

    with path.open(mode='r') as points_txt:
        content = iter(points_txt.readlines())
        for line in content:
            # literal_eval makes sure input is pure python syntax
            tuples_of_pts.append(ast.literal_eval('({0})'.format(line)))

    for line in content:
        tuples_of_pts.append(line)

    return tuples_of_pts


if __name__ == "__main__":
    import doctest
    doctest.testmod()

    print("Module0 task 1 and 2, by " + __author__ + "\n")
    print(
        "Following output is the result of checking if vector AB and AC \n" +
        "read from points.txt are oriented clockwise or counter-clockwise \n" +
        "in relation to each other.\n")

    for points in get_tuple_from_file(Path('./points.txt')):
        if is_cww(*points):
            print("CCW")
        else:
            print("CW")

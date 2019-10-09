""" Task 1 and 2 for module0 in ITA19 compas course
"""

__author__ = "Anton T Johansson"

import ast
from math import radians
from pathlib import Path

from compas.geometry import Vector, dot_vectors_xy, rotate_points_xy


def is_cww(pt_A, pt_B, pt_C):
    """ Checks if vector AB is oriented clockwise or counter-clockwise to
        vector AC.

        Parameters
        ----------
        pt_a : list or tuple of floats

        pt_b: list or tuple of floats

        pt_c: list or tuple of floats

        Returns
        -------
        None
    """
    # create the two vectors, but one is rotated 90 degrees
    # based on https://gamedev.stackexchange.com/questions/45412/
    vector_AC = Vector.from_start_end((*pt_A, 0), (*pt_C, 0))

    rot_B = rotate_points_xy([pt_B], radians(90), pt_A)
    rotated_AB = Vector.from_start_end((*pt_A, 0), *rot_B)

    # positive dot product ccw
    angle_between = dot_vectors_xy(rotated_AB, vector_AC)
    if angle_between > 0:
        print("CCW")
    elif angle_between < 0:
        print("CW")
    else:
        raise ValueError('Vectors are perpendicular')


if __name__ == "__main__":

    pt_file = Path('./points.txt')
    tuples_of_pts = []

    with pt_file.open(mode='r') as points_txt:
        content = iter(points_txt.readlines())
        for line in content:
            # literal_eval makes sure input is pure python syntax
            tuples_of_pts.append(ast.literal_eval('({0})'.format(line)))

    for line in content:
        tuples_of_pts.append(line)

    for points in tuples_of_pts:
        is_cww(points[0], points[1], points[2])

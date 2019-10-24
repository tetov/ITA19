
''' Principal component analysis
    https://en.wikipedia.org/wiki/Principal_component_analysis
    '''


from math import radians


import compas_rhino

from compas.geometry import pointcloud, Frame
from compas.geometry import bounding_box
from compas.geometry import transform_points
from compas.geometry import Rotation
from compas.geometry import Translation, Transformation
from compas.utilities import pairwise

# from compas.numerical import pca_numpy
from compas.rpc import Proxy

numerical = Proxy('compas.numerical')


def draw_cloud(cloud, bbox, color, layer):
    points = [{'pos': xyz, 'color': color} for xyz in cloud]
    lines = []
    for a, b in pairwise(bbox[:4]+bbox[:1]):
        lines.append({
            'start': a,
            'end': b,
            'color': color
        })

    for a, b in pairwise(bbox[4:]+bbox[4:5]):
        lines.append({
            'start': a,
            'end': b,
            'color': color 
        })

    for a, b in zip(bbox[4:], bbox[:4]):
        lines.append({
            'start': a,
            'end': b,
            'color': color
        })

    compas_rhino.draw_points(points, layer=layer, clear=True)
    compas_rhino.draw_lines(lines, layer=layer, clear=False)

def draw_frame(frame, layer):
    origin = list(frame.point)
    points = [{'pos': origin, 'color': (22,22,22)}]
    xaxis = list(frame.point + frame.xaxis)
    yaxis = list(frame.point+ frame.yaxis)
    zaxis = list(frame.point + frame.zaxis)
    lines = [
        {'start':origin, 'end': xaxis, 'color': (255, 0, 0)},
        {'start':origin, 'end': yaxis, 'color': (0, 255, 0)},
        {'start':origin, 'end': zaxis, 'color': (0, 0, 255)}
    ]
    compas_rhino.draw_points(points, layer=layer, clear=True)
    compas_rhino.draw_lines(lines, layer=layer, clear=False)


cloud1 = pointcloud(30, (0,10), (0,3), (0,5))
bbox1 = bounding_box(cloud1)

Rz = Rotation.from_axis_and_angle([0., 0., 1.,], radians(30))
Ry = Rotation.from_axis_and_angle([0., 1., 0.,], radians(20))
Rx = Rotation.from_axis_and_angle([1., 0., 0.,], radians(50))

T = Translation([2., 5., 8.])

R = T * Rz * Ry * Rx

cloud2 = transform_points(cloud1, Rz)
bbox2 = transform_points(bbox1, Rz)

cloud3 = transform_points(cloud1, R)
bbox3 = transform_points(bbox1, R)

mean, vectors, values = numerical.pca_numpy(cloud3)

origin = mean[0]
xaxis = vectors[0]
yaxis = vectors[1]

frame = Frame(origin, xaxis, yaxis)
world = Frame.worldXY()

X = Transformation.from_frame_to_frame(frame, world) 

cloud4 = transform_points(cloud3, X)
bbox4 = bounding_box(cloud4) 

bbox5 = transform_points(bbox4, X.inverse())



draw_cloud(cloud1, bbox1, (0,0,0), "Cloud1")
draw_cloud(cloud2, bbox2, (1,1,1), "Cloud2")
draw_cloud(cloud3, bbox3, (1,1,1), "Cloud3")
draw_cloud(cloud4, bbox4, (1,1,1), "Cloud4")
draw_cloud(cloud2, bbox5, (255, 0, 0), "Cloud5")

draw_frame(frame, "Frame")


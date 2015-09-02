from shapely.geometry import MultiPoint, Point, Polygon
import random


def reader(filename, columns=2):
    with open(filename) as f:
        for line in f:
            coords = [float(item) for item in line.split()]
            yield coords[:columns]


polly = Polygon(list(reader('polygon')))
# pointy = Point(0, 0)
# # for coords in reader('points'):
# #     point = Point(coords)
# #     print(polly.contains(point), point)
# while not polly.contains(pointy):
#     print(pointy)
#     pointy = Point(random.random()*100 for _ in range(2))

squarry = Polygon(list(reader('square')))

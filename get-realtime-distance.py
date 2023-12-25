from math import radians, cos, sin, asin, sqrt
import pprint


def distance(l1, l2, l3, l4):

    # radians which converts from degrees to radians.
    # Haversine formula

    d_lon = radians(l4) - radians(l3)
    d_lat = radians(l2) - radians(l1)
    a = sin(d_lat / 2) ** 2 + cos(l1) * cos(l2) * sin(d_lon / 2) ** 2
    c = 2 * asin(sqrt(a))

    # Radius of earth in kilometers. We can use 3956 for miles
    r = 6371

    # calculating  the result
    return c * r


# According to Location indexes
lat_longs = [
    [23.8728568, 90.3984184], [23.8513998, 90.3944536], [23.8330429, 90.4092871],
    [23.8679743, 90.3840879], [23.8248293, 90.3551134], [23.827149, 90.4106238],
    [23.8629078, 90.3816318], [23.8673789, 90.429412], [23.8248938, 90.3549467],
    [23.813316, 90.4147498]
]

g = [[0] * 10 for _ in range(10)]  # The distance between two points in form of adjacency matrix

# Loops for calculating distance between two location using their latitude and longitude
for i in range(10):  # 10 -> count of cities
    for j in range(10):  # 10 -> count of cities
        if i != j:
            lat1 = lat_longs[i][0]
            lat2 = lat_longs[j][0]
            lng1 = lat_longs[i][1]
            lng2 = lat_longs[j][1]
            g[i][j] = round(distance(lat1, lat2, lng1, lng2), 2)


print("Real time distances of mentioned bank locations using their lat and lng are:")

pprint.pprint(g)
import sys
from collections import defaultdict
from math import sin, cos, radians, acos
from operator import attrgetter
SPEED = {"metro":20,
         "bike":15,
         "foot":5}


class Attraction(object):
    def __init__(self, id, distance, speed):
        self.id = id
        self.distance = distance
        self.speed = speed
        self.time = distance/float(speed)


def parse_input(read_lines):
    N, M = -1,-1  # Initialized
    attractions = defaultdict()
    tests = list()
    for index, line in enumerate(read_lines):
        if index==0:
            N = float(line)
        elif index<=N:
            id,lat,long = line.split()  # Space separated list of id, lat, long
            attractions[int(id)] = (float(lat),float(long))
        elif index==N+1:
            M = int(line)
        else:  # index > N+1
            hotel_lat, hotel_long, transport, max_time = line.split()
            tests.append((float(hotel_lat), float(hotel_long), transport, int(max_time)))
    return N, M, attractions, tests


def distance_between(point1, point2):
    EARTH_RADIUS = 6371  # in km
    point1_lat_in_radians   = radians(point1[0])
    point2_lat_in_radians   = radians(point2[0])
    point1_long_in_radians  = radians(point1[1])
    point2_long_in_radians  = radians(point2[1]);

    distance = acos(sin(point1_lat_in_radians) * sin(point2_lat_in_radians) +
                cos(point1_lat_in_radians) * cos(point2_lat_in_radians) *
                cos(point2_long_in_radians - point1_long_in_radians)) * EARTH_RADIUS;

    return round(distance,2)


if __name__ == "__main__":
    """
    filename = sys.argv[1]
    with open(filename, 'r') as f:
    read_lines = f.readlines()
    """
    read_lines = sys.stdin.read().splitlines()
    N, M, attractions, tests = parse_input(read_lines)
    for test in tests:
        attraction_list = list()
        hotel_lat, hotel_long, transport, max_time = test
        for id, locations in attractions.iteritems():
            dist = distance_between((hotel_lat,hotel_long),attractions[id])  # in km
            time = dist/float(SPEED[transport])*60  # in minute (km/ (km/h))
            if time<=max_time:
                attraction_list.append(Attraction(id, dist, time)) # Create the object list
        sorted_attractions = sorted(attraction_list,key=attrgetter("distance","id"))
        result = [str(attr.id) for attr in sorted_attractions]
        print " ".join(result)

import sys
from collections import defaultdict, OrderedDict
from operator import attrgetter


class Hotel(object):
    def __init__(self, id, price, facilities):
        self.id = id
        self.price = price
        self.facilities = facilities
        self.num_fac = -len(facilities)  # most number of facilites start first the list


class Test(object):
    def __init__(self, max_price, min_facilities):
        self.max_price = max_price
        self.min_facilities = min_facilities


def parse_input(read_lines):
    N, M = -1,-1  # Initialized
    hotels = list()
    tests = list()
    for index, line in enumerate(read_lines):
        if index==0:
            N = float(line)
        elif index<=N:
            items = line.split()
            id, price, facilities = int(items[0]), int(items[1]), set(items[2:])  # Space separated list of id, price, facilities
            hotel = Hotel(id,price,facilities)
            hotels.append(hotel)
        elif index==N+1:
            M = int(line)
        else:  # index > N+1
            items = line.split()
            max_price, min_facilities = int(items[0]), set(items[1:])
            tests.append(Test(max_price,min_facilities))
    return N, M, hotels, tests


if __name__ == "__main__":
    read_lines = sys.stdin.read().splitlines()
    N, M, hotels, tests = parse_input(read_lines)
    for test in tests:
        hotels_list = list()
        for hotel in hotels:
            if hotel.price<=test.max_price and test.min_facilities.issubset(hotel.facilities):
                hotels_list.append(hotel)
        sorted_hotels = sorted(hotels_list,key=attrgetter("num_fac","price","id"))
        result = " ".join([str(hotel.id) for hotel in sorted_hotels])
        print result
import sys
from collections import defaultdict, OrderedDict
from operator import attrgetter


class Hotel(object):
    def __init__(self, id, price, facilities):
        self.id = id
        self.price = price
        self.facilities = facilities
        self.num_fac = -len(facilities)  # most number of facilites start first the list
        

if __name__ == "__main__":
    read_lines = sys.stdin.read().splitlines()
    N, M = -1,-1  # Initialized
    hotels = list()
    for index, line in enumerate(read_lines):
        """
        it only reads one line at a time. When the next line is read, the previous one will be garbage collected
        unless you have stored a reference to it somewhere else
        """
        if index == 0:
            N = float(line)  # Number of hotels
        elif index <= N:
            items = line.split()
            id, price, facilities = int(items[0]), int(items[1]), set(
                items[2:])  # Space separated list of id, price, facilities
            hotel = Hotel(id, price, facilities)
            hotels.append(hotel)  # Adding hotel into the hotels list
        elif index == N + 1:
            M = int(line)  # Number of test cases
        else:  # index > N+1
            """
            For each row in the tests
            """
            items = line.split()
            max_price, min_facilities = int(items[0]), set(items[1:])

            hotels_list = list()
            for hotel in hotels:
                if hotel.price<=max_price and min_facilities.issubset(hotel.facilities):
                    hotels_list.append(hotel)
            sorted_hotels = sorted(hotels_list,key=attrgetter("num_fac","price","id"))
            result = " ".join([str(hotel.id) for hotel in sorted_hotels])
            print result
import sys
from collections import defaultdict, OrderedDict
from itertools import combinations
from operator import attrgetter


class Cities(object):
    def __init__(self,cities,tags):
        self.cities = cities
        self.tags = tags
        self.num_tags = -len(self.tags)

if __name__ == "__main__":
    """
    filename = sys.argv[1]
    with open(filename, 'r') as f:
        read_lines = f.readlines()
    """
    read_lines = sys.stdin.read().splitlines()

    city_to_tag_map = defaultdict()
    tag_to_city_map = defaultdict(set)
    min_common = int(read_lines[0])
    for line in read_lines[1:]:
        city, tags = line.strip().split(":")
        tags = tags.split(",")
        city_to_tag_map[city]=set(tags)
        for tag in tags:
            tag_to_city_map[tag].add(city)

    all_tags = list(sorted(tag_to_city_map.keys()))
    set_group_cities = set()
    tags_to_cities_map = defaultdict()
    for size in range(len(all_tags),min_common-1,-1):  # sort according to size of overlapping
        for common_tags in sorted(combinations(all_tags, size)):
            cities_list = [tag_to_city_map[tag] for tag in common_tags]
            cities = sorted(reduce(set.intersection,map(set,cities_list)))
            if len(cities)>=2:
                cities = ",".join([city for city in cities])
                if (cities not in tags_to_cities_map):
                    #print cities
                    tags_to_cities_map[cities]=common_tags
                    #print ",".join(sorted(cities))+":"+",".join(common_tags)
    #print tags_to_cities_map
    #for key,val in tags_to_cities_map.items():
    #    print key+":"+",".join(val)

    cities_object_list = [Cities(key,val) for key,val in tags_to_cities_map.items()]
    for entry in sorted(cities_object_list,key=attrgetter("num_tags","cities")):
        print entry.cities + ":" + ",".join(entry.tags)
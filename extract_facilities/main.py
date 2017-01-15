import sys
if __name__ == "__main__":
    read_lines = sys.stdin.read().splitlines()
    facilities = list()
    N = -1
    for index, line in enumerate(read_lines):
        if index==0:
            N=int(line)
        if index <= N:  # parsing the list of facilities
            facilities.append(line.strip())
        else:
            description = line.strip().lower()
    # Sort the list of facilities
    facilities = sorted(facilities)
    for item in facilities:
        if item.lower() in description:
            print item
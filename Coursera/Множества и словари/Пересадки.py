Stops = list(map(int, input().split()))
first = sorted(Stops[0:2])
second = sorted(Stops[2:4])
firsty = set(range(first[0], first[1] + 1))
secondy = set(range(second[0], second[1] + 1))
print(len(firsty & secondy))

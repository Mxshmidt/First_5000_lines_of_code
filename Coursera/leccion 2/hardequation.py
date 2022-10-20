a = int(input())
b = int(input())
c = int(input())
d = int(input())
if a == b == 0:
    print("INF")
elif -b * c == -d * a or b % a != 0:
    print("NO")
else:
    print(-b // a)

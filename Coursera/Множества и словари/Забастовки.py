a, b = [int(i) for i in input().split()]
o = set(range(1, a + 1))
n = set(range(6, a + 1, 7)) | set(range(7, a + 1, 7))
st = set()
for i in range(b):
    item = [int(i) for i in input().split()]
    st = st | set(range(item[0], a + 1, item[1]))
print(len(st - n))

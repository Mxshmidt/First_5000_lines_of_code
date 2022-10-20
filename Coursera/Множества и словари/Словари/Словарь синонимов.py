N = int(input())
Sinonymy = {}
for line in range(N):
    words = input().split()
    Sinonymy[words[0]] = words[1]
    Sinonymy[words[1]] = words[0]
print(Sinonymy[input()])

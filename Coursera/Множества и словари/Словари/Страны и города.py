n = int(input())
CountriesCities = {}
Obschak = [input() for i in range(n)]
for line in Obschak:
    observed = line.split()
    Country = observed[0]
    for city in range(1, len(observed)):
        CountriesCities[observed[city]] = Country
m = int(input())
for country in range(m):
    city = input()
    print(CountriesCities[city])

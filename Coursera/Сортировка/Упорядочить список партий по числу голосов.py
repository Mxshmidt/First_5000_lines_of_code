in_file = open('input.txt', 'r', encoding='utf8')

lst = []
for line in in_file:
    lst.append(line.split('\n'))

data = []
for i in lst:
    data.append(i[0])

parties = []
votes = []
for i in data[1:data.index('VOTES:')]:
    parties.append(i)
for i in data[data.index('VOTES:') + 1:]:
    votes.append(i)

for k in parties:
    parties[parties.index(k)] = [k, votes.count(k)]


def party_sort(a):
    return -a[1], a[0]


parties.sort(key=party_sort)

for i in parties:
    print(i[0])

in_file.close()

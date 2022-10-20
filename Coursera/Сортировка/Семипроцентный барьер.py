fh = open("input.txt", "r", encoding="utf-8")
Parties = []
Votes = []
Rubicone = 0
for line in fh:
    if line.startswith("PARTIES:"):
        Rubicone = 1
        continue
    if line.startswith("VOTES:"):
        Rubicone = 2
        continue
    if Rubicone == 1:
        Parties.append(line)
    if Rubicone == 2:
        Votes.append(line)
PartiesCount = [0] * len(Parties)
for num in range(len(Parties)):
    PartiesCount[num] = Votes.count(Parties[num])
Sum = sum(PartiesCount)
for party in range(len(Parties)):
    if PartiesCount[party] / Sum * 100 > 7:
        print(Parties[party].rstrip())

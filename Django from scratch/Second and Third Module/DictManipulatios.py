toys = {'robot': 'Anton',
        'Barbie': 'Maryana',
        'dino': 'Ernur'
        }
print(*toys)
toys['dino'] = 'Anton'
for toy in toys:
    print(toys[toy], end=' ')

import itertools
print(
    *map(
        ''.join,
        itertools.permutations(
            map(
                str,
                range(
                    1,
                    int(input()) + 1
                )
            )
        )
    ), 
    sep='\n'
)

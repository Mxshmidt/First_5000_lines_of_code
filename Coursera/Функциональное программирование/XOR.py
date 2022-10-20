print(*
      map(
          int,
          map(
              lambda x: sum(x) % 2 != 0,
              zip(
                  map(
                      int,
                      input().split()
                  ),
                  map(
                      int,
                      input().split()
                  )
              )
          )
      )
      )

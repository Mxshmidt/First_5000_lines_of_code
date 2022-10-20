N = int(input())
hours = N // 3600 % 24
minutes1 = N // 60 % 60 // 10
minutes2 = N // 60 % 60 % 10
seconds1 = N % 60 // 10
seconds2 = N % 10
print(hours, ':', minutes1, minutes2, ':', seconds1, seconds2, sep='')

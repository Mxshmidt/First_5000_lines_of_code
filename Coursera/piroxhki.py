A = int(input())
B = int(input())
N = int(input())

TotalCost = ((A * 100) + B)*N
print((TotalCost // 100), (TotalCost % 100))

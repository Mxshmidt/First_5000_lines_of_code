A1, B1, C1 = int(input()), int(input()), int(input())
A2, B2, C2 = int(input()), int(input()), int(input())
# ввод всевозможных количеств
S1 = (A1 // A2) * (B1 // B2) * (C1 // C2)
S2 = (A1 // A2) * (B1 // C2) * (C1 // B2)
S3 = (A1 // B2) * (B1 // A2) * (C1 // C2)
S4 = (A1 // C2) * (B1 // A2) * (C1 // B2)
S5 = (A1 // C2) * (B1 // B2) * (C1 // A2)
S6 = (A1 // B2) * (B1 // C2) * (C1 // A2)
# сортировка первых трех
if S1 <= S3:
    S1, S3 = S3, S1
if S1 <= S2:
    S1, S2 = S2, S1
# сортировка вторых трех
if S4 <= S6:
    S4, S6 = S6, S4
if S4 <= S5:
    S4, S5 = S5, S4
# общая сортировка
if S1 <= S4:
    S1, S4 = S4, S1
print(S1)

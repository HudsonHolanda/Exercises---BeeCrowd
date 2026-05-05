A, B, C = map(int, input().split())

Maior_ab = int((A + B + abs(A - B)) / 2)
Maior_abc = int((Maior_ab + C + abs(Maior_ab - C)) / 2)

print(f"{Maior_abc} eh o maior")
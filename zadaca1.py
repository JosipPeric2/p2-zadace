import random

n = 7
matrica = []

for i in range(n):
    red = []
    for j in range(n):
        broj = random.randint(1, 9)
        red.append(broj)
    matrica.append(red)

print("Generirana matrica:")
for red in matrica:
    print(red)
    
zbroj_rubova = 0

for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            zbroj_rubova += matrica[i][j]

print("\nZbroj elemenata na rubovima matrice je:", zbroj_rubova)
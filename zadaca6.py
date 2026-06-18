def parni_brojevi(granica):
    for i in range(granica):
        if i % 2 == 0:
            yield i

def neparni_brojevi(granica):
    for i in range(granica):
        if i % 2 != 0:
            yield i

print("Parni:")
for broj in parni_brojevi(10):
    print(broj, end=" ")

print("\nNeparni:")
for broj in neparni_brojevi(10):
    print(broj, end=" ")
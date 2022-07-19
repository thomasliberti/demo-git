"""
doc
"""
nterms = int(input("Entrez un nombre: "))

N1 = 0
N2 = 1

print("\n la suite fibonacci est :")
print(N1, ",", N2, end=", ")

for i in range(2, nterms):
    C0 = N1 + N2
    print(C0, end=", ")

    N1 = N2
    N2 = C0
    
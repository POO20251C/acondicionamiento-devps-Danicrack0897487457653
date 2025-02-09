#1
numero = input()
suma = 0
for d in numero:
    if d.isdigit():
        suma += int(d)
print(suma)

#2
cadena = input().lower()
vocales = "aeiou"
contador = 0
for c in cadena:
    if c in vocales:
        contador += 1
print(contador)

#3
cadena = input().replace(" ", "").lower()
if cadena == cadena[::-1]:
    print("Si")
else:
    print("No")

#4
numeros = input().split()
print(" ".join(numeros[::-1]))

#5
cadena = input().split()
print(len(cadena))

#6
numeros = list(map(int, input().split()))
print(max(numeros), min(numeros))



#Daniel Amelines Pacheco

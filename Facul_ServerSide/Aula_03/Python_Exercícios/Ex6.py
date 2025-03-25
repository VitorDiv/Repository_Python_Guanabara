""""
Crie um programa que encontre o maior número em uma lista
usando um loop for.
"""

numeros = [100, 12, 7, 25, 5, 8, 19]

maior_numero = numeros[0]

for numero in numeros:
    if numero > maior_numero:
        maior_numero = numero

print("O maior número da lista é:", maior_numero)


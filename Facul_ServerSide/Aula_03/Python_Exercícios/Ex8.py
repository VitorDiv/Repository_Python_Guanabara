'''
Crie um programa que remova todos os elementos duplicados de uma lista
usando um loop for.
'''

lista = [1, 2, 2, 3, 4, 4, 5]
lista_sem_duplicatas = []

for item in lista:
    if item not in lista_sem_duplicatas:
        lista_sem_duplicatas.append(item)

print(lista_sem_duplicatas)

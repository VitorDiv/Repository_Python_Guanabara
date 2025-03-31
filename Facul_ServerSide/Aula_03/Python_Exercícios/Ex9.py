'''
Escreva um programa que verifique se uma lista está em ordem crescente
usando um loop for.
'''

lista1 = [1, 2, 3, 4, 5, 6, 7]
em_ordem = True 

for i in range(len(lista1)-1):  
    if lista1[i] > lista1[i + 1]:
        em_ordem = False 
        break 

if em_ordem:
    print('A lista está em ordem crescente')
else:
    print('A lista NÃO está em ordem crescente')

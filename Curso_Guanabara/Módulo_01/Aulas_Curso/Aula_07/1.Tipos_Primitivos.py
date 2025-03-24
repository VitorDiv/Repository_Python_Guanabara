# [+] Adição
# [-] Subtração
# [*] Multiplicação
# [/] Divisão
# [**] Potência
# [//] Divisão Inteira 
# [%] Resto da Divisão

# Ordem Precedência
# [()]
# [**]
# [*] [/] [//] [%]
# [+] [-]

nome = input('Qual é seu nome? ')
print(f'Prazer em te conhecer, {nome:<20}!') # garante por exemplo um espaço de 20 caracteres após o nome 
print(f'Prazer em te conhecer, {nome:=^20}!') # Printa  =======vitor========!

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite um segundo valor: '))
print(f'A soma vale {n1 + n2}', end=' >>>') # End serve para não dar a quebra de linha, se usar /n quebra linha
print (' Teste Concluído')

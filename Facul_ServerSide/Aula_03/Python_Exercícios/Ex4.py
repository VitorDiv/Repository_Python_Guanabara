#Crie um programa que itere por uma string 
#e conte o número de vogais.

palavra = 'Vitor'

vogais = 0
for x in palavra:
    if x.upper() in ['A', 'E', 'I', 'O', 'U']:
        vogais += 1

print("Número de vogais:", vogais)



"""
Escreva um programa que inverta uma string usando um loop for.
"""
texto = "Python"
texto_invertido = ""

for i in range(len(texto) - 1, -1, -1):
    texto_invertido += texto[i]

print("Texto invertido:", texto_invertido)



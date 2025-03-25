"""
Escreva um programa que inverta uma string usando um loop for.
"""

# String original
texto = "Python"

# Variável para armazenar a string invertida
texto_invertido = ""

# Loop para percorrer a string de trás para frente
for i in range(len(texto) - 1, -1, -1):
    texto_invertido += texto[i]

# Exibir a string invertida
print("Texto invertido:", texto_invertido)

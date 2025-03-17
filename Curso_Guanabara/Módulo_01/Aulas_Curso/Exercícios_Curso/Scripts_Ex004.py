#programa em Python que solicita ao usuário uma entrada e, em seguida, exibe informações sobre os tipos primitivos dessa entrada

entrada = input("Digite algo: ")

print(f"\nInformações sobre a entrada '{entrada}':")
print(f"Tipo: {type(entrada)}")
print(f"É numérico? {entrada.isdigit()}")
print(f"É alfabético? {entrada.isalpha()}")
print(f"É alfanumérico? {entrada.isalnum()}")
print(f"É maiúsculo? {entrada.isupper()}")
print(f"É minúsculo? {entrada.islower()}")
print(f"Está vazio? {len(entrada) == 0}")
print(f"É espaço em branco? {entrada.isspace()}")

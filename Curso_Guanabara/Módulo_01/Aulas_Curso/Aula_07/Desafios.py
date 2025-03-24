
# Faça um programa que leia um número intero e mostre seu sucessor e antecessor 

n1 = int(input('Digite um número: '))

print('o antecessor do núemro digitado é: ',(n1 - 1))
print('o sucessor do núemro digitado é: ',(n1 + 1))

#----------------------------------------------------#

# Algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada

n2 = float(input('Digite um número, e calcularei o [dobro], [triplo], [raiz quadrada]: '))

print('o dobro do número digitado é:', n2 * 2)
print('o triplo do número digitado é:', n2 * 3)
print('a raiz quadrada do número digitado é:', n2 ** 0.5)


#----------------------------------------------------#

# Algoritmo que leia 2 número e calcule a média

print('Vamos calcular sua média?')
n1_1 = float(input('Digite a primeira nota: '))
n2_2 = float(input('Digite a primeira nota: '))

media = (n1_1 + n2_2) / 2
print('A média das notas informadas é: ', media)

#----------------------------------------------------#

# Algoritmo que leia um valor em metros e tranforme convertendo em centímetros e milímitros

print('Vamos coverter os números?')

Numero = float(input('Digite um valor em metros: '))

print('O valor convertido em centímetros é: ', Numero * 100)
print('O valor convertido em milimítros é: ', Numero * 1000)


#----------------------------------------------------#

# Algoritmo que leia o número intero e faça a tabuada dele

print('Vamos calcular a tabuada de um número inteiro?')
N = int(input('Dígite um número inteiro: '))

for i in range (1,11):
 print(f'{N} x {i} = {N * i}')

#----------------------------------------------------#

# Programa quanto dinheiro uma pessoa tem na carteira e quantos dólares pode comprar
# considere, US$ 1.00 = 3,27

print('Calculando quantos doláres é possivél comprar com uma quantia em real')

Total = float(input('Digite o valor em carteira: '))
print(f'é possivél comprar, US$ {Total / 3.27:.2f}')


#----------------------------------------------------#

# Algoritmo para ler a largura e altura de uma parede em metros
# --> Calcular à area
# --> Quantidade de Tinta [ cada litro de tinta pinta 2mt Quadrados]

print('Vamos calculcar a largura e altura de sua parede, e a quantidade de tinta')

p1 = int(input('Digite a largura da parede: '))
p2 = int(input('Digite a altura da parede da parede: '))

S = p1 * p2

print(f'A sua parede ao total possui {S} Metros Quadrados, e será necessário {S / 2} latas de tinta para a pintura!')


#----------------------------------------------------#

# Faça um programa que leia o preço de um produto e mostre seu preço com 5% de desconto

preco = float(input('Preço do produto: '))
desconto = preco * 0.05
descontofinal = preco - desconto 
print(f'o preço do produto com 5% de desconto é {descontofinal}')


#----------------------------------------------------#

# Algoritmo que leia o salário do funcionario e mostre o mesmo com 15% de aumento

salario = float(input('Digite o seu salário: '))
aumento = salario * 0.15
salariofinal = salario + aumento
print(f'o salaário final com o aumento é de {salariofinal}')

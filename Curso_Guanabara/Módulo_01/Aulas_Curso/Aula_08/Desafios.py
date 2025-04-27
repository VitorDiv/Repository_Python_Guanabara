#-----------------------------------------------------#

#Leia um número real, e mostre apenas a porção inteira
from math import trunc
num = float(input('Digite um número: '))
print(f'a parte inteira digitada foi {trunc(num)}')

#-----------------------------------------------------#

#Calcule o comprimento do cateto adjacente de um triângulo retângulo, mostre comprimento da hipotenusa
from math import hypot
n1 = int(input('Dígite um número: '))
n2 = int(input('Dígite um número: '))

print(f'a hipotenusa dos números digitado é {hypot(n1,n2):.0f}')

#-----------------------------------------------------#


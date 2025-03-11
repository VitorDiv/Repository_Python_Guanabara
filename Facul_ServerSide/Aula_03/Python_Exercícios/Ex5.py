#Escreva um programa que imprima os primeiros 10 números da sequência 
#de Fibonacci usando um loop for.

n = 10

a, b = 0, 1

for i in range(n):
    print(a)  
    a, b = b, a + b  
##Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

Letra = str(input('digite uma letra para verificar se é consoante ou vogal: ')).upper()

if Letra == ['a','e','i','o','u']:
    print ('Você digitou uma vogal')
else:
    print('Você digitou uma consoante')
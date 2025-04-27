# Em Python, **módulos** são arquivos que contêm definições e códigos em Python
# que podem ser reutilizados em outros programas. Eles ajudam a organizar e reutilizar código.

# Para usar os recursos de um módulo, existem duas formas principais:

# 1. import nome_do_módulo
#    - Importa o módulo inteiro. Para acessar algo do módulo, usamos: nome_do_módulo.objeto
#    - Exemplo: import random
#               num = random.randint(1, 10)

# 2. from nome_do_módulo import objeto
#    - Importa apenas o(s) objeto(s) que você especificar (função, classe, variável).
#    - Exemplo: from random import randint
#               num = randint(1, 10)

# --------------------------------------------
# Exemplo com o módulo random
# --------------------------------------------

import random  # Importa o módulo completo chamado 'random'

# Gera um número inteiro aleatório entre 1 e 10 (inclusive)
num = random.randint(1, 10)

print(num)  # Exibe o número sorteado

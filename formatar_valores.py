"""

:s - texto (strings)
:d - inteiros (int)
:f - números de pontos flutuantes (float)
:.(NÚMERO)f - quantidade de casas decimais (float)
:(CARACTERE) (> ou < ou ^) (QUANTIDADE) (TIPO - s, d ou f)

> - esquerda
< - direita
^ - centro


"""

num1 = 5
num2 = 4

divisao = num1 / num2

print('{:.2f}'.format(divisao)) # :.2f representa a quantidade de casas decimais

print('{:.3f}'.format(divisao))  # Aqui usamos :.f3 para que apareçam 3 casas decimais

# outra maneira de fazer o código

print( f'{divisao:.2f}')

print( f'{divisao:.3f}')

#####

nome = "Alan Angeli"

print(f'{nome:s}')

#####

num3 = 1
print(f'{num3:0>10}')
print(f'{num3:1>10}')
print(f'{num3:2>10}')

num4 = 1150

print(f"{num4:0>10}") # > deixam os 0 a esquerda
print(f"{num4:0<10}") # < deixam os 0 a direita
print(f"{num4:0^10}") # ^ deixa a variável no centro e os 0 divididos na esquerda e direita

print(f"{num4:0>10.2f}") # adicionando duas casas decimais

print(f"{nome:#^50}") # também funciona com string
print( (50 - len(nome)) / 2) # contar os caractéres

nome_formatado = "{:#^50}".format(nome) # outra forma de escrever o código
print(nome_formatado)

nome2 = "Alan Neves"
nome2_formatado = "{n:0<20}".format(n=nome2)
print(nome2_formatado)

######



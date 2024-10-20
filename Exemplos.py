# Variáveis, Tipos e Conversão
a = 10
b = 3.14
c = "Hello"
d = True

# Conversão de tipos
a_str = str(a)
b_int = int(b)
c_bool = bool(c)
d_float = float(d)

# Operadores
soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
modulo = a % b
potencia = a ** 2

# Tabelas Verdade
verdadeiro = True
falso = False

and_result = verdadeiro and falso
or_result = verdadeiro or falso
not_result = not verdadeiro

# Listas
lista = [1, 2, 3, 4, 5]
lista.append(6)
lista.remove(3)
lista[0] = 10

# Tuplas
tupla = (1, 2, 3, 4, 5)
primeiro_elemento = tupla[0]

# Dicionários
dicionario = {"chave1": "valor1", "chave2": "valor2"}
dicionario["chave3"] = "valor3"
valor = dicionario["chave1"]

# Conjuntos
conjunto = {1, 2, 3, 4, 5}
conjunto.add(6)
conjunto.remove(3)

# Expressões e Variáveis
x = 5
y = 10
expressao = (x + y) * 2

# Strings
string = "Hello, World!"
substring = string[0:5]
string_upper = string.upper()
string_lower = string.lower()

# Condicional if
if a > b:
    resultado = "a é maior que b"
else:
    resultado = "a não é maior que b"

# Exemplo 1
if c == "Hello":
    resultado = "A string é Hello"

# Exemplo 2
if d:
    resultado = "d é verdadeiro"

# Exemplo 3
if a > 0 and b > 0:
    resultado = "a e b são positivos"

# Comando de Repetição While
contador = 0
while contador < 5:
    print(contador)
    contador += 1

# Repetição For
for i in range(5):
    print(i)

# Funções
def soma(a, b):
    return a + b

resultado_soma = soma(5, 3)

# Funções lambda
soma_lambda = lambda x, y: x + y
resultado_lambda = soma_lambda(5, 3)

# Outras Funções
def saudacao(nome):
    return f"Olá, {nome}!"

mensagem = saudacao("Mundo")
print(mensagem)
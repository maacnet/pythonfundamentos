# nomes.py
from nome_funcao import formatar_nome
print("Pressione a letra q para sair")
while True:
    nome = input("Digite o seu nome: ")
    if nome == 'q':
        break
    sobrenome = input("Digite o seu sobrenome: ")
    if sobrenome == 'q':
        break
    nome_completo = formatar_nome(nome,sobrenome)
    print(f"Olá, {nome_completo}!")
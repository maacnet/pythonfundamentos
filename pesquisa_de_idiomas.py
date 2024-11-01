# pesquisa_de_idiomas.py
from pesquisa import PesquisaAnonima

# Define uma pergunta e cria uma pesquisa.
pergunta = "Qual idioma você aprendeu a falar primeiro?"
pesquisa_idiomas = PesquisaAnonima(pergunta)

# Mostra a pergunta e armazena as respostas.
pesquisa_idiomas.mostrar_pergunta()
print("Digite 'q' a qualquer momento para sair.\n")
while True:
    resposta = input("Idioma: ")
    if resposta == 'q':
        break
    pesquisa_idiomas.armazenar_resposta(resposta)

# Mostra os resultados da pesquisa.
print("\nObrigado a todos que participaram da pesquisa!")
pesquisa_idiomas.mostrar_resultados()
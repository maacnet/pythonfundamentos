# test_pesquisa_de_idiomas.py
from pesquisa import PesquisaAnonima
def test_pergunta():
    pergunta = "Qual idioma você aprendeu a falar primeiro?"
    pesquisa_idiomas = PesquisaAnonima(pergunta)
    assert pesquisa_idiomas.pergunta == pergunta
# pesquisa.py
class PesquisaAnonima:
    """Coleta respostas anônimas para uma pergunta de pesquisa."""

    def __init__(self, pergunta):
        """Armazena uma pergunta e prepara para armazenar respostas."""
        self.pergunta = pergunta
        self.respostas = []

    def mostrar_pergunta(self):
        """Mostra a pergunta da pesquisa."""
        print(self.pergunta)

    def armazenar_resposta(self, nova_resposta):
        """Armazena uma única resposta para a pesquisa."""
        self.respostas.append(nova_resposta)

    def mostrar_resultados(self):
        """Mostra todas as respostas que foram dadas."""
        print("Resultados da pesquisa:")
        for resposta in self.respostas:
            print(f"- {resposta}")
# Escrevendo um teste unitário
# test_nome_funcao.py
from nome_funcao import formatar_nome
def test_formatar_nome():
    nome_completo = formatar_nome('Marco','Carvalho')
    assert nome_completo == 'Marco Carvalho'
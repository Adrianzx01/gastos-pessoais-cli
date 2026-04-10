import pytest
from src.operacoes import validar_valor, calcular_total


# TESTE 1: Caminho Feliz (Sucesso)
def test_calcular_total_sucesso():
    gastos = [
        {"descricao": "Almoço", "valor": 30.0},
        {"descricao": "Transporte", "valor": 20.0}
    ]
    assert calcular_total(gastos) == 50.0


# TESTE 2: Entrada Inválida (Erro esperado)
def test_validar_valor_negativo_erro():
    with pytest.raises(ValueError, match="O valor deve ser maior que zero."):
        validar_valor(-5)


# TESTE 3: Caso Limite (Vazio)
def test_calcular_total_lista_vazia():
    assert calcular_total([]) == 0

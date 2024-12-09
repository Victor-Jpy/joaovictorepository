import datetime

from meu_modulo.finances_class import Transaction

def test_instancia():
    transaction = Transaction(1200, "investimento", "ser um vendedor")

    assert isinstance(transaction, Transaction)

def test_value_type():
    transaction = Transaction(1200.00, "investimento, ", "ser um vendedor")

    assert isinstance(Transaction.amount, float)
    assert Transaction.amount == 1200.00
    assert isinstance(Transaction.category, str)
    assert Transaction.category == "investimento"
    assert isinstance(Transaction.description, str)
    assert Transaction.description == "ser um vendedor"

def test_impressao():
    impressao = Transaction(1200.00, "investimento, ", "ser um vendedor")

    assert str(impressao) == "Transacao: ser um vendedor R$ 0,00:1200.00 (investimento)"

def test_update():
    transacao = Transaction(1200.00, "investimento", "ser um vendedor")
    dicty = {"amount": 2000.00, "category": "moradia", "description:": "lugar melhor"}

    transacao = Transaction.update(dicty)

    assert transacao.amount == 2000.00
    assert transacao.category == "moradia"
    assert transacao.description == "lugar melhor"


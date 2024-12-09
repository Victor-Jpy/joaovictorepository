from meu_modulo.finances_class import Transaction, Investiment, Account, Client

transacao = Transaction(2500.00, "saude", "consulta medica")
print(transacao)

dicty = {}
transacao = Transaction.update({"amount": 4000.00, "category": "moradia", "description:": "lugar melhor"})
print(transacao)
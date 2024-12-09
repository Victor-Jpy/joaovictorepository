import datetime 

class Transaction:
    date = datetime.datetime.now()

    def __init__(self, amount: float, category: str, description: str = "") -> None:
        self.amount = amount
        self.category = category
        self.description = ""

    def __str__(self) -> str:
        return f"Transacao: {self.description}R$ {0,00:self.amount} ({self.category})"
    
    def update(self, atributes ):
        for key, value in atributes.items():
            if hasattr(self, key):
                setattr(self, key, value)

class Account:
    def __init__(self, name: str) -> None:
        self.name = name
    
    def add_transaction(self, amount: float, category: int, description: str = "") -> Transaction:
        self.amount = amount
        self.category = category
        self.description = ""

    def get_transactions(self, start_date: datetime = None, end_date: datetime = None, category: int = None) -> list[Transaction]:
        pass

    def client(self, client):
        self.client = client

class Investiment:
    date_puschased = datetime.datetime.now()

    def __init__(self, type: int, amount: float, rate_of_return: float) -> None:
        self.type = type
        self.amount = amount
        self.rate_of_return = rate_of_return

    def calculate_value(self):
        pass

    def sell(self, Account):
        pass

class Client:
    def __init__(self, name: str):
        self.name = name

    def add_account(self, account_name: str) -> Account:
        pass

    def add_investment(self, investment: Investiment) -> None:
        pass

    def get_net_worth(self) -> float:
        pass


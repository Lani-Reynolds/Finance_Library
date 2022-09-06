class Item:
    def __init__(self, name, flat_price, quantity) -> None:
        self.name: str
        self.flat_price: float
        self.quantity: int
        self.cost_plus_percentage: float = 0.12
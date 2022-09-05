from dataclasses import dataclass

@dataclass
class Item:
    name: str
    flat_price: float
    quantity: int
    # inflation: float
    cost_plus_percentage: float = 0.50

@dataclass
class Production_Order:
    order: list
    assets: list = None
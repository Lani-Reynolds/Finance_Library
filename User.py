class User:
    def __init__(self, name) -> None:
        self.name: str = name
        self.total_assets: list = []
        
    def Add_To_Assets(self, order) -> None:
        self.total_assets.append(order)
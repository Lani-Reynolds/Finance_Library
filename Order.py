class Order:
    def __init__(self, order_format, order) -> None:
        self.order_format = order_format
        self.order = order
        self.assets = None
        
    def ReadOrder(self):
        if self.order_format == "CSV":
            pass
        if self.order_format == "TXT":
            pass

    def Cost_Of_Goods(self, order):

        return sum([round((item.flat_price * item.quantity), 2) for item in order])

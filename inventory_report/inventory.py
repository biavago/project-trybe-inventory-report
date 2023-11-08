from inventory_report.product import Product


class Inventory:
    def __init__(self, data: list[Product] or None = None):
        if data is None:
            data = []
        else:
            self.data = data

    @property
    def data(self):
        self.data

    def add_data(self, data: list[Product]) -> None:
        self.data += data

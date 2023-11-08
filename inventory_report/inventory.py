from inventory_report.product import Product


class Inventory:
    # pass
    def __init__(self, data: list[Product] or None = None):
        if data is None:
            return self.data
        else:
            self.data = []

    @property
    def data(self) -> list[Product]:
        return self.data

    def add_data(self, data: list[Product]) -> None:
        for product in data:
            return self.data.append(product)

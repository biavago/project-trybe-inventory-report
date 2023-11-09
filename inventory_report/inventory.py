from inventory_report.product import Product


class Inventory:
    # pass
    def __init__(self, data: list[Product] or None = None):
        if data is None:
            data = []
        self._data = data

    def add_data(self, data: list[Product]) -> None:
        for product in data:
            self._data.append(product)

    @property
    def data(self) -> list[Product]:
        return self._data

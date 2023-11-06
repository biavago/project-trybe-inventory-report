from abc import ABC, abstractmethod
from inventory_report.product import Product
from typing import Dict, Type
import json


class Importer(ABC):
    # pass
    def __init__(self, path: str) -> None:
        self.path = path

    @abstractmethod
    def import_data(self) -> list[Product]:
        pass


class JsonImporter(Importer):
    # pass
    def __init__(self, path: str) -> None:
        super().__init__(path)

    def import_data(self) -> list[Product]:
        result = []

        with open(self.path, 'r') as file:
            data = json.load(file)

        for product in data:
            list_item = Product(
                product["id"],
                product["product_name"],
                product["company_name"],
                product["manufacturing_date"],
                product["expiration_date"],
                product["serial_number"],
                product["storage_instructions"],
            )
            result.append(list_item)

        return result


class CsvImporter:
    pass


# Não altere a variável abaixo

IMPORTERS: Dict[str, Type[Importer]] = {
    "json": JsonImporter,
    "csv": CsvImporter,
}

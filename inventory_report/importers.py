from typing import Dict, Type
from abc import abstractmethod, ABC
from inventory_report.product import Product
import json


class Importer(ABC):
    def __init__(self, path: str):
        self.path = path

    @abstractmethod
    def import_data(self) -> list[Product]:
        pass


class JsonImporter(Importer):
    def __init__(self, path: str):
        super().__init__(path)

    def import_data(self) -> list[Product]:
        with open(self.path, "r") as json_file:
            json_data = json.load(json_file)
            list_of_products = []
            for product in json_data:
                list_of_products.append(
                    Product(
                        id=product["id"],
                        product_name=product["product_name"],
                        company_name=product["company_name"],
                        manufacturing_date=product["manufacturing_date"],
                        expiration_date=product["expiration_date"],
                        serial_number=product["serial_number"],
                        storage_instructions=product["storage_instructions"],
                    )
                )
            return list_of_products


class CsvImporter:
    pass


# Não altere a variável abaixo

IMPORTERS: Dict[str, Type[Importer]] = {
    "json": JsonImporter,
    "csv": CsvImporter,
}

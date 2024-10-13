from typing import Dict, Type, List
from abc import abstractmethod, ABC
from inventory_report.product import Product
import json
import csv


class Importer(ABC):
    def __init__(self, path: str):
        self.path = path

    @abstractmethod
    def import_data(self) -> List[Product]:
        pass


class JsonImporter(Importer):
    def import_data(self) -> List[Product]:
        with open(self.path, "r") as file:
            data = json.load(file)

        products = [
            Product(
                id=item["id"],
                product_name=item["product_name"],
                company_name=item["company_name"],
                manufacturing_date=item["manufacturing_date"],
                expiration_date=item["expiration_date"],
                serial_number=item["serial_number"],
                storage_instructions=item["storage_instructions"],
            )
            for item in data
        ]

        return products


class CsvImporter(Importer):
    def import_data(self) -> List[Product]:
        products = []
        with open(self.path, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                product = Product(
                    id=row["id"],
                    product_name=row["product_name"],
                    company_name=row["company_name"],
                    manufacturing_date=row["manufacturing_date"],
                    expiration_date=row["expiration_date"],
                    serial_number=row["serial_number"],
                    storage_instructions=row["storage_instructions"],
                )
                products.append(product)
        return products


# Não altere a variável abaixo
IMPORTERS: Dict[str, Type[Importer]] = {
    "json": JsonImporter,
    "csv": CsvImporter,
}
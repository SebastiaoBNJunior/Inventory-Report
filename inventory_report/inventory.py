from typing import List, Optional
from inventory_report.product import Product


class Inventory:
    def __init__(self, data: Optional[List[Product]] = None) -> None:
        self.__data = data or []


    @property
    def data(self) -> List[Product]:
        return self.__data

    def add_data(self, data: List[Product]) -> None:
        self.data.extend(data)
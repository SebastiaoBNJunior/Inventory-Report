import datetime
from typing import List
from inventory_report.inventory import Inventory
from inventory_report.product import Product
from inventory_report.reports.report import Report


class SimpleReport():

    def __init__(self) -> None:
        self.stock: List[Product] = []

    def add_inventory(self, inventory: Inventory) -> None: 
        self.stock.extend(inventory.data)

    @staticmethod
    def conversion_date(date: str) -> datetime.date:
        return datetime.datetime.strptime(date, "%Y-%m-%d").date()

    def generate(self) -> str: 

        oldest_manufacturing = min(self.stock, key=lambda p: self.conversion_date(p.manufacturing_date)).manufacturing_date
        closest_expiration = min(
            (p for p in self.stock if self.conversion_date(p.expiration_date) > datetime.datetime.now().date()),
            key=lambda p: self.conversion_date(p.expiration_date)
        ).expiration_date

        count_product = {}
        for product in self.stock:
                company = product.company_name
                if company in count_product:
                    count_product[company] += 1
                else: 
                     count_product[company] = 1

        company_max_inventory = max(count_product, key=count_product.get)

        expect_return = (
            f"Oldest manufacturing date: {oldest_manufacturing}\n"
            f"Closest expiration date: {closest_expiration}\n"
            f"Company with the largest inventory: {company_max_inventory}"
        )

        return expect_return

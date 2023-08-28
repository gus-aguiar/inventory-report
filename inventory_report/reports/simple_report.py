from inventory_report.inventory import Inventory
from datetime import datetime


class SimpleReport:
    def __init__(self) -> None:
        self.stock: list[Inventory] = []

    def add_inventory(self, inventory: Inventory) -> None:
        self.stock.append(inventory)

    def get_companies_inventories(self) -> dict[str, int]:
        inventory_size_counts: dict[str, int] = {}
        for inventory in self.stock:
            for product in inventory.data:
                if product.company_name in inventory_size_counts:
                    inventory_size_counts[product.company_name] += 1
                else:
                    inventory_size_counts[product.company_name] = 1
        return inventory_size_counts

    def get_biggest_company(self) -> str:
        inventory_sizes = self.get_companies_inventories()
        company = 0
        name = ""
        for companies in inventory_sizes:
            if inventory_sizes[companies] > company:
                company = inventory_sizes[companies]
                name = companies
        return name

    def get_oldest_date(self) -> str:
        oldest_date = ""
        for inventory in self.stock:
            for product in inventory.data:
                if oldest_date == "":
                    oldest_date = product.manufacturing_date
                if product.manufacturing_date < oldest_date:
                    oldest_date = product.manufacturing_date
        return oldest_date

    def get_closest_date(self) -> str:
        datetime_format = "%Y-%m-%d"
        current_date = datetime.now().date()
        closest_date = None

        for inventory in self.stock:
            for product in inventory.data:
                expiration_date = datetime.strptime(
                    product.expiration_date, datetime_format
                ).date()
                if expiration_date > current_date and (
                    closest_date is None or expiration_date < closest_date
                ):
                    closest_date = expiration_date

        if closest_date is not None:
            return closest_date.strftime("%Y-%m-%d")
        else:
            return "No future expiration dates found"

    def generate(self) -> str:
        return (
            f"Oldest manufacturing date: {self.get_oldest_date()} \n"
            f"Closest expiration date: {self.get_closest_date()} \n"
            f"Company with the largest inventory: "
            f"{self.get_biggest_company()} \n"
        )

from inventory_report.reports.simple_report import SimpleReport
from collections import OrderedDict


class CompleteReport(SimpleReport):
    def get_companies_inventories_ordered(self) -> str:
        inventory_size_counts = super().get_companies_inventories()

        ordered_inventory_counts = OrderedDict(
            sorted(
                inventory_size_counts.items(), key=lambda x: x[1], reverse=True
            )
        )

        result = ""
        for company, count in ordered_inventory_counts.items():
            result += f"- {company}: {count}\n"

        return result

    def generate(self) -> str:
        return (
            f"Oldest manufacturing date: {self.get_oldest_date()}\n"
            f"Closest expiration date: {self.get_closest_date()}\n"
            f"Company with the largest inventory: "
            f"{self.get_biggest_company()}\n"
            f"Stocked products by company:\n"
            f"{self.get_companies_inventories_ordered()}\n"
        )

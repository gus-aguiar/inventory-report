from inventory_report.product import Product


class Inventory:
    def __init__(self, data: list[Product] | None = None) -> None:
        if data is None:
            self._data = []
        else:
            self._data = data

    def add_data(self, data: list[Product]) -> None:
        self.data.extend(data)

    @property
    def data(self) -> list[Product]:
        return self._data

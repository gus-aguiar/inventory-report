from inventory_report.product import Product


def test_product_report() -> None:
    product = Product(
        id="1",
        product_name="product name",
        company_name="company name",
        manufacturing_date="2022-01-01",
        expiration_date="2023-01-01",
        serial_number="123456",
        storage_instructions="Instructions",
    )
    assert product.__str__() == (
        f"The product {product.id} - {product.product_name} "
        f"with serial number {product.serial_number} "
        f"manufactured on {product.manufacturing_date} "
        f"by the company {product.company_name} "
        f"valid until {product.expiration_date} "
        "must be stored according to the following instructions: "
        f"{product.storage_instructions}."
    )

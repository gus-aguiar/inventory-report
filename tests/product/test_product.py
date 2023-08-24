from inventory_report.product import Product


def test_create_product() -> None:
    product = Product(
        id="1",
        product_name="product name",
        company_name="company name",
        manufacturing_date="2022-01-01",
        expiration_date="2023-01-01",
        serial_number="123456",
        storage_instructions="Instructions",
    )
    assert product.id == "1"
    assert product.product_name == "product name"
    assert product.company_name == "company name"
    assert product.manufacturing_date == "2022-01-01"
    assert product.expiration_date == "2023-01-01"
    assert product.serial_number == "123456"
    assert product.storage_instructions == "Instructions"


# initial commit

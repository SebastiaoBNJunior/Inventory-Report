from inventory_report.product import Product

def test_create_product():
    product = Product(
        id="1234",
        product_name="Test Product",
        company_name="Test Company",
        manufacturing_date="2023-01-01",
        expiration_date="2024-01-01",
        serial_number="SN1234",
        storage_instructions="Keep in a cool, dry place."
    )

    assert product.id == "1234"
    assert product.product_name == "Test Product"
    assert product.company_name == "Test Company"
    assert product.manufacturing_date == "2023-01-01"
    assert product.expiration_date == "2024-01-01"
    assert product.serial_number == "SN1234"
    assert product.storage_instructions == "Keep in a cool, dry place."
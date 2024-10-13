from inventory_report.product import Product


def test_product_report():
    product = Product(
        id="1",
        product_name="farinha",
        company_name="Farinini",
        manufacturing_date="01-05-2021",
        expiration_date="02-06-2023",
        serial_number="TY68 409C JJ43 ASD1 PL2F",
        storage_instructions="precisa ser armazenado em local protegido da luz",
    )

    expected_report = (
        "The product 1 - farinha with serial number TY68 409C JJ43 ASD1 PL2F "
        "manufactured on 01-05-2021 by the company Farinini valid until 02-06-2023 "
        "must be stored according to the following instructions: "
        "precisa ser armazenado em local protegido da luz."
    )

    assert str(product) == expected_report
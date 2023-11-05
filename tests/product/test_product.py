from inventory_report.product import Product


def test_create_product() -> None:
    product_test = Product(
        "1",
        "Chocolate",
        "Lindt",
        "02/11/2023",
        "02/11/2025",
        "111222333",
        "Temperatura ambiente"
    )

    assert product_test.id == "1"
    assert product_test.product_name == "Chocolate"
    assert product_test.company_name == "Lindt"
    assert product_test.manufacturing_date == "02/11/2023"
    assert product_test.expiration_date == "02/11/2025"
    assert product_test.serial_number == "111222333"
    assert product_test.storage_instructions == "Temperatura ambiente"

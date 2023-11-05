from inventory_report.product import Product


def test_product_report() -> None:
    product_test = Product(
        "1",
        "Chocolate",
        "Lindt",
        "02/11/2023",
        "02/11/2025",
        "112233",
        "Conservar em temperatura ambiente e protegido da luz"
    )
    # mudança no serial number para a linha não ficar muito longa
    # f"The product {self.id} - {self.product_name} "
    # f"with serial number {self.serial_number} "
    # f"manufactured on {self.manufacturing_date} "
    # f"by the company {self.company_name} "
    # f"valid until {self.expiration_date} "
    # "must be stored according to the following instructions: "
    # f"{self.storage_instructions}."

    assert (
        str(product_test)
        == "The product 1 - Chocolate with serial number 112233 manufactured "
        "on 02/11/2023 by the company Lindt valid until 02/11/2025 "
        "must be stored according to the following instructions: "
        "Conservar em temperatura ambiente e protegido da luz."
    )

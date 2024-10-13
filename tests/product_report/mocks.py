from inventory_report.product import Product


class _TestMockProductInvalidStringOnFirstLine(Product):
    def __str__(self) -> str:
        return super().__str__().replace("The product", "hello")


class _TestMockProductInvalidStringOnSecondLine(Product):
    def __str__(self) -> str:
        return super().__str__().replace("with serial number", "welcome")


class _TestMockProductInvalidStringOnThirdLine(Product):
    def __str__(self) -> str:
        return super().__str__().replace("manufactured", "to")


class _TestMockProductInvalidStringOnFourthLine(Product):
    def __str__(self) -> str:
        return super().__str__().replace("by", "the")


class _TestMockProductInvalidStringOnFifthLine(Product):
    def __str__(self) -> str:
        return super().__str__().replace("valid until", "Trybe")


class _TestMockProductInvalidStringOnSixthLine(Product):
    def __str__(self) -> str:
        return (
            super()
            .__str__()
            .replace(
                "must be stored according to the following instructions",
                "side",
            )
        )


class _TestMockProductInvalidId(Product):
    def __str__(self) -> str:
        return super().__str__().replace(self.id, "invalid id")


class _TestMockProductInvalidName(Product):
    def __str__(self) -> str:
        return super().__str__().replace(self.product_name, "invalid name")


class _TestMockProductInvalidSerialNumber(Product):
    def __str__(self) -> str:
        return super().__str__().replace(self.serial_number, "inv number")


class _TestMockProductInvalidCompanyName(Product):
    def __str__(self) -> str:
        return super().__str__().replace(self.company_name, "invalid name")


class _TestMockProductInvalidManufacturingDate(Product):
    def __str__(self) -> str:
        return (
            super().__str__().replace(self.manufacturing_date, "invalid date")
        )


class _TestMockProductInvalidExpirationDate(Product):
    def __str__(self) -> str:
        return super().__str__().replace(self.expiration_date, "invalid date")


class _TestMockProductInvalidStorageInstructions(Product):
    def __str__(self) -> str:
        return (
            super()
            .__str__()
            .replace(self.storage_instructions, "invalid instructions")
        )

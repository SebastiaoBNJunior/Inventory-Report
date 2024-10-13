class _TestMockProductWithoutId:
    def __init__(
        self,
        id: str,
        product_name: str,
        company_name: str,
        manufacturing_date: str,
        expiration_date: str,
        serial_number: str,
        storage_instructions: str,
    ):
        self.product_name = product_name
        self.company_name = company_name
        self.manufacturing_date = manufacturing_date
        self.expiration_date = expiration_date
        self.serial_number = serial_number
        self.storage_instructions = storage_instructions


class _TestMockProductWithInvalidId:
    def __init__(
        self,
        id: str,
        product_name: str,
        company_name: str,
        manufacturing_date: str,
        expiration_date: str,
        serial_number: str,
        storage_instructions: str,
    ):
        self.id = "invalid_id"
        self.product_name = product_name
        self.company_name = company_name
        self.manufacturing_date = manufacturing_date
        self.expiration_date = expiration_date
        self.serial_number = serial_number
        self.storage_instructions = storage_instructions


class _TestMockProductWithoutProductName:
    def __init__(
        self,
        id: str,
        product_name: str,
        company_name: str,
        manufacturing_date: str,
        expiration_date: str,
        serial_number: str,
        storage_instructions: str,
    ):
        self.id = id
        self.company_name = company_name
        self.manufacturing_date = manufacturing_date
        self.expiration_date = expiration_date
        self.serial_number = serial_number
        self.storage_instructions = storage_instructions


class _TestMockProductWithInvalidProductName:
    def __init__(
        self,
        id: str,
        product_name: str,
        company_name: str,
        manufacturing_date: str,
        expiration_date: str,
        serial_number: str,
        storage_instructions: str,
    ):
        self.id = id
        self.product_name = "invalid_product_name"
        self.company_name = company_name
        self.manufacturing_date = manufacturing_date
        self.expiration_date = expiration_date
        self.serial_number = serial_number
        self.storage_instructions = storage_instructions


class _TestMockProductWithoutCompanyName:
    def __init__(
        self,
        id: str,
        product_name: str,
        company_name: str,
        manufacturing_date: str,
        expiration_date: str,
        serial_number: str,
        storage_instructions: str,
    ):
        self.id = id
        self.product_name = product_name
        self.manufacturing_date = manufacturing_date
        self.expiration_date = expiration_date
        self.serial_number = serial_number
        self.storage_instructions = storage_instructions


class _TestMockProductWithInvalidCompanyName:
    def __init__(
        self,
        id: str,
        product_name: str,
        company_name: str,
        manufacturing_date: str,
        expiration_date: str,
        serial_number: str,
        storage_instructions: str,
    ):
        self.id = id
        self.product_name = product_name
        self.company_name = "invalid_company_name"
        self.manufacturing_date = manufacturing_date
        self.expiration_date = expiration_date
        self.serial_number = serial_number
        self.storage_instructions = storage_instructions


class _TestMockProductWithoutManufacturingDate:
    def __init__(
        self,
        id: str,
        product_name: str,
        company_name: str,
        manufacturing_date: str,
        expiration_date: str,
        serial_number: str,
        storage_instructions: str,
    ):
        self.id = id
        self.product_name = product_name
        self.company_name = company_name
        self.expiration_date = expiration_date
        self.serial_number = serial_number
        self.storage_instructions = storage_instructions


class _TestMockProductWithInvalidManufacturingDate:
    def __init__(
        self,
        id: str,
        product_name: str,
        company_name: str,
        manufacturing_date: str,
        expiration_date: str,
        serial_number: str,
        storage_instructions: str,
    ):
        self.id = id
        self.product_name = product_name
        self.company_name = company_name
        self.manufacturing_date = "invalid_manufacturing_date"
        self.expiration_date = expiration_date
        self.serial_number = serial_number
        self.storage_instructions = storage_instructions


class _TestMockProductWithoutExpirationDate:
    def __init__(
        self,
        id: str,
        product_name: str,
        company_name: str,
        manufacturing_date: str,
        expiration_date: str,
        serial_number: str,
        storage_instructions: str,
    ):
        self.id = id
        self.product_name = product_name
        self.company_name = company_name
        self.manufacturing_date = manufacturing_date
        self.serial_number = serial_number
        self.storage_instructions = storage_instructions


class _TestMockProductWithInvalidExpirationDate:
    def __init__(
        self,
        id: str,
        product_name: str,
        company_name: str,
        manufacturing_date: str,
        expiration_date: str,
        serial_number: str,
        storage_instructions: str,
    ):
        self.id = id
        self.product_name = product_name
        self.company_name = company_name
        self.manufacturing_date = manufacturing_date
        self.expiration_date = "invalid_expiration_date"
        self.serial_number = serial_number
        self.storage_instructions = storage_instructions


class _TestMockProductWithoutSerialNumber:
    def __init__(
        self,
        id: str,
        product_name: str,
        company_name: str,
        manufacturing_date: str,
        expiration_date: str,
        serial_number: str,
        storage_instructions: str,
    ):
        self.id = id
        self.product_name = product_name
        self.company_name = company_name
        self.manufacturing_date = manufacturing_date
        self.expiration_date = expiration_date
        self.storage_instructions = storage_instructions


class _TestMockProductWithInvalidSerialNumber:
    def __init__(
        self,
        id: str,
        product_name: str,
        company_name: str,
        manufacturing_date: str,
        expiration_date: str,
        serial_number: str,
        storage_instructions: str,
    ):
        self.id = id
        self.product_name = product_name
        self.company_name = company_name
        self.manufacturing_date = manufacturing_date
        self.expiration_date = expiration_date
        self.serial_number = "invalid_serial_number"
        self.storage_instructions = storage_instructions


class _TestMockProductWithoutStorageInstructions:
    def __init__(
        self,
        id: str,
        product_name: str,
        company_name: str,
        manufacturing_date: str,
        expiration_date: str,
        serial_number: str,
        storage_instructions: str,
    ):
        self.id = id
        self.product_name = product_name
        self.company_name = company_name
        self.manufacturing_date = manufacturing_date
        self.expiration_date = expiration_date
        self.serial_number = serial_number


class _TestMockProductWithInvalidStorageInstructions:
    def __init__(
        self,
        id: str,
        product_name: str,
        company_name: str,
        manufacturing_date: str,
        expiration_date: str,
        serial_number: str,
        storage_instructions: str,
    ):
        self.id = id
        self.product_name = product_name
        self.company_name = company_name
        self.manufacturing_date = manufacturing_date
        self.expiration_date = expiration_date
        self.serial_number = serial_number
        self.storage_instructions = "invalid_storage_instructions"

from typing import Generator
from unittest.mock import patch

import pytest
from pytest_dependency import build_mocked_assets

from inventory_report.product import Product
from tests.product import mocks
from tests.product.test_product import test_create_product

mocking = build_mocked_assets(
    mocks_module=mocks,
    asset_to_mock=Product,
    test_function=test_create_product,
    custom_exceptions={
        mocks._TestMockProductWithoutId: AttributeError,
        mocks._TestMockProductWithoutProductName: AttributeError,
        mocks._TestMockProductWithoutCompanyName: AttributeError,
        mocks._TestMockProductWithoutManufacturingDate: AttributeError,
        mocks._TestMockProductWithoutExpirationDate: AttributeError,
        mocks._TestMockProductWithoutSerialNumber: AttributeError,
        mocks._TestMockProductWithoutStorageInstructions: AttributeError,
    },
)


# Teste do requisito 1
@pytest.fixture(autouse=True, params=mocking)
def mock_it(request: pytest.FixtureRequest) -> Generator[None, None, None]:
    with patch(
        "tests.product.test_product.Product",
        request.param,
    ):
        yield

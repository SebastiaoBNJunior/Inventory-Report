from typing import Generator
from unittest.mock import patch

import pytest
from pytest_dependency import build_mocked_assets

from inventory_report.product import Product
from tests.product_report import mocks
from tests.product_report.test_product_report import test_product_report

mocking = build_mocked_assets(
    mocks_module=mocks,
    asset_to_mock=Product,
    test_function=test_product_report,
)


# Teste do requisito 2
@pytest.fixture(autouse=True, params=mocking)
def mock_it(request: pytest.FixtureRequest) -> Generator[None, None, None]:
    with patch(
        "tests.product_report.test_product_report.Product",
        request.param,
    ):
        yield

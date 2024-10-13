from typing import List

import pytest

from inventory_report.inventory import Inventory
from inventory_report.product import Product


@pytest.mark.dependency
def test_init_receive_self_and_data() -> None:
    inventory_init_params = Inventory.__init__.__code__.co_varnames
    assert "self" in inventory_init_params
    assert "data" in inventory_init_params
    assert Inventory.__init__.__code__.co_argcount == 2


@pytest.mark.dependency
def test_init_data_is_an_optional_list_of_products() -> None:
    data_annotation = str(Inventory.__init__.__annotations__["data"]).replace(
        "typing.List", "list"
    )

    expected_values = [
        "typing.Union[list[inventory_report.product.Product], NoneType]",
        "typing.Optional[list[inventory_report.product.Product]]",
        "None | list[inventory_report.product.Product]",
        "list[inventory_report.product.Product] | None",
    ]
    assert data_annotation in expected_values


@pytest.mark.dependency
def test_init_data_default_value_is_none() -> None:
    assert Inventory.__init__.__defaults__ == (None,)


@pytest.mark.dependency
def test_data_generate_new_list_when_default_value_is_used() -> None:
    inventory_1 = Inventory()
    inventory_2 = Inventory()
    assert inventory_1.data == []
    assert inventory_2.data == []
    assert inventory_1.data is not inventory_2.data


@pytest.mark.dependency
def test_data_receive_list_of_products(
    products: List[Product],
) -> None:
    inventory = Inventory(products)
    assert inventory.data == products


@pytest.mark.dependency
def test_data_is_read_only(products: List[Product]) -> None:
    inventory = Inventory()
    with pytest.raises(AttributeError):
        inventory.data = products  # type: ignore


@pytest.mark.dependency
def test_add_data_is_a_list_of_products() -> None:
    assert (
        str(Inventory.add_data.__annotations__["data"]).replace(
            "typing.List", "list"
        )
        == "list[inventory_report.product.Product]"
    )


@pytest.mark.dependency
def test_add_data(products: List[Product]) -> None:
    inventory = Inventory()
    inventory.add_data(products)
    assert inventory.data == products


# Teste do requisito 5
@pytest.mark.dependency(
    depends=[
        "test_init_receive_self_and_data",
        "test_init_data_is_an_optional_list_of_products",
        "test_init_data_default_value_is_none",
        "test_data_generate_new_list_when_default_value_is_used",
        "test_data_receive_list_of_products",
        "test_data_is_read_only",
        "test_add_data_is_a_list_of_products",
        "test_add_data",
    ]
)
def test_inventory_final() -> None:
    pass

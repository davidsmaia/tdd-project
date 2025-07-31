from typing import List
from uuid import UUID

import pytest
from store.schemas.product import ProductOut, ProductUpdateOut
from store.usecases.product import product_usecase
from store.core.exceptions import BaseException, NotFoundException


async def test_usecases_create_should_return_sucess(product_in):
    result = await product_usecase.create(body=product_in)

    assert isinstance(result, ProductOut)
    assert result.name == "Iphone 14 Pro Max"

async def test_usecases_get_should_return_sucess(product_inserted):
    result = await product_usecase.get(id=product_inserted.id)

    assert isinstance(result, ProductOut)
    assert result.name == "Iphone 14 Pro Max"

async def test_usecases_get_shout_not_found():
    
    with pytest.raises(NotFoundException) as err:
        await product_usecase.get(id=UUID("70547edd-5837-4219-a6b7-9d05c05777df"))

    assert (err.value.message == "Product not found with filter: 70547edd-5837-4219-a6b7-9d05c05777df")

@pytest.mark.usefixtures("products_inserted")
async def test_usecases_query_should_return_sucess():
    result = await product_usecase.query()

    assert isinstance(result, List)
    assert len(result) > 1

async def test_usecases_update_should_return_sucess(product_up, product_inserted):
    product_up.price = 7.500
    result = await product_usecase.update(id=product_inserted.id, body=product_up)


    assert isinstance(result, ProductUpdateOut)


async def test_usecases_delete_should_return_sucess(product_inserted):
    result = await product_usecase.delete(id=product_inserted.id)

    assert result is True

async def test_usecases_delete_shout_not_found():
    
    with pytest.raises(NotFoundException) as err:
        await product_usecase.delete(id=UUID("70547edd-5837-4219-a6b7-9d05c05777df"))

    assert (err.value.message == "Product not found with filter: 70547edd-5837-4219-a6b7-9d05c05777df")

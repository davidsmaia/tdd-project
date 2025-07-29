from pydantic import Field
from store.core.schemas.base import BaseSchemaMixin


class ProductIn(BaseSchemaMixin):
    # No pydantic, os tres pontos (...) dizem q o valor é obrigatório - ou seja, que deve ser passado
    name: str = Field(...,description="Product name") 
    quantity: int = Field(...,description="Product quantity")
    price: float = Field(...,description="Product price")
    status: bool = Field(...,description="Product status")
from abc import ABCMeta, abstractmethod
from dataclasses import dataclass
from typing import List


@dataclass
class ProductItem:
    id: int
    name: str
    description: str


class _ProductShop(metaclass=ABCMeta):

    @abstractmethod
    def get_product(self) -> List[ProductItem]: ...

    @abstractmethod
    def add_product(self, item: ProductItem): ...


class BookShop(_ProductShop):
    id = 1
    name = "First Book Shop"

    def __init__(self):
        self._produts: List[ProductItem] = []

    def get_product(self) -> List[ProductItem]:
        return self._produts

    def add_product(self, item: ProductItem):
        self._produts.append(item)

    def find_by_id(self, product_id: int):
        for product in self._produts:
            if product.id == product_id:
                return product

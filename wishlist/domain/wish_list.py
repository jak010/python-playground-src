from __future__ import annotations

import uuid
from typing import List

from .wish_item import WishItem


class WishList:

    def __init__(self, customer_id: int):
        self.id = str(uuid.uuid4())
        self.customer_id = customer_id

        self._lines: List[WishItem] = []

    def add_line(self, wish_item: WishItem):
        self._lines.append(wish_item)

    def __repr__(self):
        return f"WishList({self.id})"

    def __iter__(self):
        for _item in self._lines:
            yield _item

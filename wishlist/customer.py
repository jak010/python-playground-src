from __future__ import annotations

from dataclasses import dataclass, field
from typing import List

from domain import WishList


@dataclass
class Customer:
    id: int
    name: str
    wish_lists: List[WishList] = field(default_factory=list)

    def wishlist_summary(self):
        _report = {}
        for wish_list in self.wish_lists:
            for item in wish_list:
                if item.shop_name not in _report:
                    _report[item.shop_name] = item.quantity
                else:
                    _report[item.shop_name] += item.quantity

        print(_report)

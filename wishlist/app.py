from __future__ import annotations

from customer import Customer
from domain import WishList, WishItem
from product_shop import ProductItem, BookShop

if __name__ == '__main__':
    shop = BookShop()
    shop.add_product(
        item=ProductItem(id=1, name="첫 번쨰 상품이올시다", description="test")
    )

    customer = Customer(id=1, name='test')

    wish_list = WishList(customer_id=customer.id)
    wish_list.add_line(
        wish_item=WishItem(shop_id=shop.id, shop_name=shop.name, product=shop.find_by_id(product_id=1), quantity=2))
    wish_list.add_line(
        wish_item=WishItem(shop_id=shop.id, shop_name=shop.name, product=shop.find_by_id(product_id=1), quantity=3))

    customer.wish_lists.append(wish_list)

    print(customer.wishlist_summary())

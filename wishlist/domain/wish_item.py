class WishItem:

    def __init__(self, shop_id, shop_name, product, quantity):
        self.shop_id = shop_id
        self.shop_name = shop_name
        self.product = product
        self.quantity = quantity

    def __repr__(self):
        return f"WishItem(" \
               f" shop_id={self.shop_id}" \
               f" shop_name={self.shop_name}" \
               f" product={self.product}" \
               f" quantity={self.quantity}" \
               f")"

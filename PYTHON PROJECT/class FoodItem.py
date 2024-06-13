class FoodItem:
    def __init__(self, item_id, name, price):
        self.item_id = item_id
        self.name = name
        self.price = price

    def __repr__(self):
        return f"FoodItem(id={self.item_id}, name={self.name}, price={self.price})"

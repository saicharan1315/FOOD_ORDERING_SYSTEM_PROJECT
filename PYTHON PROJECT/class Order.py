class Order:
    def __init__(self, order_id, customer):
        self.order_id = order_id
        self.customer = customer
        self.items = []

    def add_item(self, food_item):
        self.items.append(food_item)

    def remove_item(self, item_id):
        self.items = [item for item in self.items if item.item_id != item_id]

    def __repr__(self):
        items_list = "\n".join([f"  - {item.item_id}: {item.name} (${item.price:.2f})" for item in self.items])
        return f"Order ID: {self.order_id}\nItems:\n{items_list}\n"
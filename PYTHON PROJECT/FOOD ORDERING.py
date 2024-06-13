class FoodItem:
    def __init__(self, item_id, name, price):
        self.item_id = item_id
        self.name = name
        self.price = price

    def __repr__(self):
        return f"FoodItem(id={self.item_id}, name={self.name}, price={self.price})"


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


class Customer:
    def __init__(self, customer_id, name):
        self.customer_id = customer_id
        self.name = name

    def __repr__(self):
        return f"Customer(id={self.customer_id}, name={self.name})"


class FoodOrderingSystem:
    def __init__(self):
        self.food_items = {}
        self.orders = {}
        self.next_order_id = 1

    def add_food_item(self, item_id, name, price):
        if item_id not in self.food_items:
            self.food_items[item_id] = FoodItem(item_id, name, price)
            return True
        return False

    def update_food_item(self, item_id, name, price):
        if item_id in self.food_items:
            self.food_items[item_id].name = name
            self.food_items[item_id].price = price
            return True
        return False

    def remove_food_item(self, item_id):
        if item_id in self.food_items:
            del self.food_items[item_id]
            return True
        return False

    def view_food_items(self):
        return list(self.food_items.values())

    def place_order(self, customer):
        order = Order(self.next_order_id, customer)
        self.orders[self.next_order_id] = order
        self.next_order_id += 1
        return order.order_id

    def view_orders(self):
        return list(self.orders.values())

    def update_order(self, order_id, action, food_item=None):
        if order_id in self.orders:
            order = self.orders[order_id]
            if action == "add" and food_item:
                order.add_item(food_item)
                return True
            elif action == "remove" and food_item:
                order.remove_item(food_item.item_id)
                return True
        return False

    def cancel_order(self, order_id):
        if order_id in self.orders:
            del self.orders[order_id]
            return True
        return False


# Function to display the menu
def display_menu(system):
    print("Food Menu:")
    for item in system.view_food_items():
        print(f"{item.item_id}. {item.name} - ${item.price:.2f}")
    print()


# Function to handle placing an order
def place_order(system, customer):
    order_id = system.place_order(customer)
    print(f"Order ID: {order_id}")
    while True:
        display_menu(system)
        item_id = int(input("Enter the food item ID to add to the order (0 to finish): "))
        if item_id == 0:
            break
        if item_id in system.food_items:
            system.update_order(order_id, "add", system.food_items[item_id])
        else:
            print("Invalid food item ID.")
    print(f"Thank you for your order, {customer.name}!")
    return order_id


# Function to view all orders
def view_orders(system):
    print("All Orders:")
    for order in system.view_orders():
        print(order)
    print()


# Function to handle restaurant owner login
def owner_login():
    username = "owner"
    password = "password"
    input_username = input("Enter username: ")
    input_password = input("Enter password: ")
    if input_username == username and input_password == password:
        return True
    else:
        print("Invalid credentials. Access denied.")
        return False


# Main function to run the food ordering system
def main():
    system = FoodOrderingSystem()
    system.add_food_item(1, "Burger", 5.99)
    system.add_food_item(2, "Pizza", 7.99)
    system.add_food_item(3, "Soda", 1.99)

    while True:
        print("1. Customer")
        print("2. Restaurant Owner")
        print("3. Exit")
        user_type = int(input("Enter your choice: "))

        if user_type == 1:
            customer = Customer(1, "SAI")
            while True:
                print("1. Place an order")
                print("2. View all orders")
                print("3. Cancel an order")
                print("4. Exit")
                choice = int(input("Enter your choice: "))

                if choice == 1:
                    place_order(system, customer)
                elif choice == 2:
                    view_orders(system)
                elif choice == 3:
                    order_id = int(input("Enter the order ID to cancel: "))
                    if system.cancel_order(order_id):
                        print("ORDER HAS BEEN CANCELLED")
                    else:
                        print("Order ID not found.")
                elif choice == 4:
                    break
                else:
                    print("Invalid choice. Please try again.")

        elif user_type == 2:
            if owner_login():
                while True:
                    print("1. Add food item")
                    print("2. Update food item")
                    print("3. Remove food item")
                    print("4. View food items")
                    print("5. Exit")
                    choice = int(input("Enter your choice: "))

                    if choice == 1:
                        item_id = int(input("Enter food item ID: "))
                        name = input("Enter food item name: ")
                        price = float(input("Enter food item price: "))
                        if system.add_food_item(item_id, name, price):
                            print("Food item added successfully.")
                        else:
                            print("Food item with this ID already exists.")
                    elif choice == 2:
                        item_id = int(input("Enter food item ID: "))
                        name = input("Enter new food item name: ")
                        price = float(input("Enter new food item price: "))
                        if system.update_food_item(item_id, name, price):
                            print("Food item updated successfully.")
                        else:
                            print("Food item with this ID does not exist.")
                    elif choice == 3:
                        item_id = int(input("Enter food item ID to remove: "))
                        if system.remove_food_item(item_id):
                            print("Food item removed successfully.")
                        else:
                            print("Food item with this ID does not exist.")
                    elif choice == 4:
                        print("Food Items:")
                        for item in system.view_food_items():
                            print(item)
                    elif choice == 5:
                        break
                    else:
                        print("Invalid choice. Please try again.")

        elif user_type == 3:
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

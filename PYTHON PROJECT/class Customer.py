class Customer:
    def __init__(self, customer_id, name):
        self.customer_id = customer_id
        self.name = name

    def __repr__(self):
        return f"Customer(id={self.customer_id}, name={self.name})"
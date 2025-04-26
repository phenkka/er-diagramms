import sqlite3
from datetime import datetime

class ExampleInsert():
    def __init__(self, name, users_data, products_data, orders_data, order_items_data):
        self.conn = sqlite3.connect(name)
        self.cursor = self.conn.cursor()

        self.insert_table(
            data=users_data,
            query="""
                INSERT INTO Users(is_active, username, registration_date, password)
                VALUES(?, ?, ?, ?);
            """
        )

        self.insert_table(
            data=products_data,
            query="""
                INSERT INTO Products(name, description, price, category, created_at)
                VALUES (?, ?, ?, ?, ?);
            """
        )

        self.insert_table(
            data=orders_data,
            query="""
                INSERT INTO Orders(user_id, order_date, total_amount)
                VALUES (?, ?, ?);
            """
        )

        self.insert_table(
            data=order_items_data,
            query="""
                INSERT INTO OrderItems(order_id, product_id, quantity, unit_price)
                VALUES (?, ?, ?, ?);
            """
        )

        self.conn.commit()

    def insert_table(self, data, query):
        self.conn.executemany(query, data)

    def close(self):
        self.conn.close()


if __name__ == "__main__":
    users_data = [
        (True, "leonardo_dicaprio", datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "password1"),
        (False, "meryl_streep", datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "password2"),
        (True, "robert_downey_jr", datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "password3"),
        (True, "tom_hanks", datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "password4"),
        (True, "scarlett_johansson", datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "password5"),
        (False, "brad_pitt", datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "password6"),
        (True, "will_smith", datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "password7"),
        (True, "natalie_portman", datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "password8"),
        (True, "johnny_depp", datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "password9"),
        (False, "denzel_washington", datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "password10")
    ]

    products_data = [
        ("Laptop", "High-end gaming laptop", 1599.99, "Electronics", datetime.now().strftime('%Y-%m-%d %H:%M:%S')),
        ("Smartphone", "Flagship smartphone", 999.99, "Electronics", datetime.now().strftime('%Y-%m-%d %H:%M:%S')),
        ("Wireless Headphones", "Noise cancelling headphones", 249.99, "Electronics",
         datetime.now().strftime('%Y-%m-%d %H:%M:%S')),
        ("Mechanical Keyboard", "RGB mechanical keyboard", 129.99, "Accessories",
         datetime.now().strftime('%Y-%m-%d %H:%M:%S')),
        ("Gaming Mouse", "Precision gaming mouse", 59.99, "Accessories", datetime.now().strftime('%Y-%m-%d %H:%M:%S')),
        ("4K Monitor", '27" Ultra HD monitor', 349.99, "Electronics", datetime.now().strftime('%Y-%m-%d %H:%M:%S')),
        ("Power Bank", "20000mAh power bank", 39.99, "Accessories", datetime.now().strftime('%Y-%m-%d %H:%M:%S')),
        ("Smartwatch", "Fitness tracking smartwatch", 149.99, "Electronics",
         datetime.now().strftime('%Y-%m-%d %H:%M:%S')),
        ("Bluetooth Speaker", "Waterproof speaker", 89.99, "Accessories", datetime.now().strftime('%Y-%m-%d %H:%M:%S')),
        ("DSLR Camera", "Professional DSLR camera", 899.99, "Electronics", datetime.now().strftime('%Y-%m-%d %H:%M:%S')),
        ("Sofa", "Comfortable 3-seater sofa", 499.99, "Home", datetime.now().strftime('%Y-%m-%d %H:%M:%S')),
        ("Coffee Table", "Wooden coffee table", 147.99, "Home", datetime.now().strftime('%Y-%m-%d %H:%M:%S')),
        ("Microwave Oven", "30L convection microwave", 199.99, "Home Appliances",
         datetime.now().strftime('%Y-%m-%d %H:%M:%S')),
        ("Air Conditioner", "Energy-efficient AC", 599.99, "Home Appliances",
         datetime.now().strftime('%Y-%m-%d %H:%M:%S')),
        ("Sneakers", "Running sneakers", 87.99, "Clothing", datetime.now().strftime('%Y-%m-%d %H:%M:%S')),
        ("Jacket", "Waterproof jacket", 119.99, "Clothing", datetime.now().strftime('%Y-%m-%d %H:%M:%S')),
        ("Backpack", "Travel backpack", 79.99, "Accessories", datetime.now().strftime('%Y-%m-%d %H:%M:%S')),
        ("Book: Python 101", "Beginner programming guide", 29.99, "Books", datetime.now().strftime('%Y-%m-%d %H:%M:%S')),
        ("Book: AI Future", "Advanced AI concepts", 34.99, "Books", datetime.now().strftime('%Y-%m-%d %H:%M:%S')),
        ("Desk Lamp", "LED study lamp", 24.99, "Home", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    ]

    orders_data = [
        (3, datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 1599.99 + 59.99*4),
        (4, datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 249.99 + 129.99*2),
        (5, datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 1599.99*2 + 249.99),
        (1, datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 249.99 + 59.99*4),
        (7, datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 149.99 + 79.99*3),
        (1, datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 129.99*2 + 79.99),
        (3, datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 899.99*3 + 249.99),
        (8, datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 1599.99*2 + 129.99),
        (9, datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 999.99 + 59.99*5),
        (4, datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 249.99 + 39.99*10),
        (8, datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 349.99 + 249.99*2),
        (5, datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 499.99 + 149.99*5),
        (1, datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 1599.99 + 999.99),
        (3, datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 129.99*3 + 349.99*2),
        (9, datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 129.99 + 499.99),
    ]

    order_items_data = [
        (1, 1, 1, 1599.99),
        (1, 5, 4, 59.99),
        (2, 3, 1, 249.99),
        (2, 4, 2, 129.99),
        (3, 1, 2, 1599.99),
        (3, 3, 1, 249.99),
        (4, 3, 1, 249.99),
        (4, 5, 4, 59.99),
        (5, 8, 1, 149.99),
        (5, 17, 3, 79.99),
        (6, 4, 2, 129.99),
        (6, 17, 1, 79.99),
        (7, 10, 3, 899.99),
        (7, 3, 1, 249.99),
        (8, 1, 2, 1599.99),
        (8, 4, 1, 129.99),
        (9, 2, 1, 999.99),
        (9, 5, 5, 59.99),
        (10, 3, 1, 249.99),
        (10, 7, 10, 39.99),
        (11, 6, 1, 349.99),
        (11, 3, 2, 249.99),
        (12, 11, 1, 499.99),
        (12, 8, 5, 149.99),
        (13, 1, 1, 1599.99),
        (13, 2, 1, 999.99),
        (14, 4, 3, 129.99),
        (14, 6, 2, 349.99),
        (15, 4, 1, 129.99),
        (15, 11, 1, 499.99),
    ]

    db = ExampleInsert("database.db", users_data, products_data, orders_data, order_items_data)
    db.close()
import sqlite3

class ExampleSelect:
    def __init__(self, name):
        self.conn = sqlite3.connect(name)
        self.cursor = self.conn.cursor()

    def close(self):
        self.conn.close()

    def execute_read_many_query(self, query, params=None):
        result = None
        try:
            self.cursor.execute(query, params or ())
            if self.cursor.description:
                cols = [col[0] for col in self.cursor.description]
                rows = self.cursor.fetchall()
                result = [dict(zip(cols, row)) for row in rows]
        except Exception as e:
            print(f"An error occurred: {e}")
        return result

    def get_top_5_users(self):
        query = """
            SELECT Users.user_id, Users.username, SUM(Orders.total_amount) AS total_spent
            FROM Users
            JOIN Orders ON Users.user_id = Orders.user_id
            GROUP BY Users.user_id
            ORDER BY total_spent DESC
            LIMIT 5;
        """

        result = self.execute_read_many_query(query)
        return result

    def get_top_5_products(self):
        query = """
            SELECT Products.name, SUM(OrderItems.quantity) AS total_quantity
            FROM OrderItems
            JOIN Products ON OrderItems.product_id = Products.product_id
            GROUP BY Products.name
            ORDER BY total_quantity DESC
            LIMIT 5;       
        """
        result = self.execute_read_many_query(query)
        return result

    def get_category_price_stats(self):
        query = """
            SELECT category, MIN(price) AS min_price, MAX(price) AS max_price, AVG(price) AS avg_price
            FROM Products
            WHERE price > 0
            GROUP BY category
            ORDER BY avg_price DESC;
        """

        result = self.execute_read_many_query(query)
        return result

    def get_avg_amount_per_user(self):
        query = """
            SELECT Users.username, AVG(Orders.total_amount) AS avg_order_amount
            FROM Users
            JOIN Orders ON Users.user_id = Orders.user_id
            GROUP BY Users.username
            HAVING COUNT(Orders.order_id) > 1
            ORDER BY avg_order_amount DESC;
        """

        result = self.execute_read_many_query(query)
        return result

    def get_expencive_products_then_avg(self):
        query = """
            SELECT name, category, price
            FROM Products
            WHERE price > (
                SELECT AVG(price)
                FROM Products
                WHERE category = Products.category
            )
            ORDER BY category, price DESC;
        """

        result = self.execute_read_many_query(query)
        return result
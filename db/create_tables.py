import sqlite3

class CreateTables:
    def __init__(self, name):
        self.conn = sqlite3.connect(name)
        self.cursor = self.conn.cursor()
        self.cursor.execute("PRAGMA foreign_keys = ON;")

    def create_tables(self):
        queries = [
            """
            CREATE TABLE IF NOT EXISTS Users(
                user_id INTEGER PRIMARY KEY,
                is_active BOOLEAN,
                username TEXT,
                registration_date TIMESTAMP,
                password TEXT
                );
            """,
            """
            CREATE TABLE IF NOT EXISTS Products(
                product_id INTEGER PRIMARY KEY,
                name TEXT,
                description TEXT,
                price REAL,
                category TEXT,
                created_at TIMESTAMP
            );
            """,
            """
            CREATE TABLE IF NOT EXISTS Orders(
                order_id INTEGER PRIMARY KEY,
                user_id INTEGER,
                order_date TIMESTAMP,
                total_amount INTEGER,
                FOREIGN KEY (user_id) REFERENCES Users(user_id)
            );
            """,
            """
            CREATE TABLE IF NOT EXISTS OrderItems(
                item_id INTEGER PRIMARY KEY,
                order_id INTEGER,
                product_id INTEGER,
                quantity INTEGER,
                unit_price REAL,
                FOREIGN KEY (order_id) REFERENCES Orders(order_id),
                FOREIGN KEY (product_id) REFERENCES Products(product_id)
            );
            """
        ]

        for query in queries:
            self.cursor.execute(query)

        self.conn.commit()

    def close_conn(self):
        self.conn.close()

if __name__ == "__main__":
    db = CreateTables("database.db")
    db.create_tables()
    db.close_conn()
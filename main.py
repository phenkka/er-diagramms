import pandas as pd
from db.example_select import ExampleSelect


class Tracker:
    def __init__(self, path):
        self.db = ExampleSelect(path)

    def show_menu(self):
        print(
            "1 - Show top 5 users by spending.\n"
            "2 - Show top 5 most popular products.\n"
            "3 - Show price statistics by category.\n"
            "4 - Show average spending per user.\n"
            "5 - Show products more expensive than average.\n"
            "6 - Exit.\n"
        )

    def wait_for_back(self) -> None:
        input("\nPress Enter to return to the menu... 🔙\n")

    def print_table(self, header, func, ps):
        print(f"\n{header}\n")
        df = pd.DataFrame(func)
        print(df.to_string(index=False))
        print(f"\n{ps}")
        self.wait_for_back()

    def run(self):
        while True:
            self.show_menu()
            choice = input("\nWhat would you like to do? (1-6) 🤔\n")

            if choice == "1":
                self.print_table(
                    header="Top 5 users by spending:",
                    func=self.db.get_top_5_users(),
                    ps="P.S. 🤑 Big spenders spotted!"
                )
            elif choice == "2":
                self.print_table(
                    header="Top 5 most popular products:",
                    func=self.db.get_top_5_products(),
                    ps="P.S. 🎯 Looks like everyone loves these!"
                )
            elif choice == "3":
                self.print_table(
                    header="Price statistics by category:",
                    func=self.db.get_category_price_stats(),
                    ps="P.S. 📊 Numbers never lie!"
                )
            elif choice == "4":
                self.print_table(
                    header="Average spending per user:",
                    func=self.db.get_avg_amount_per_user(),
                    ps="P.S. 🧮 Time to budget smarter!"
                )
            elif choice == "5":
                self.print_table(
                    header="Products priced above average:",
                    func=self.db.get_expencive_products_then_avg(),
                    ps="P.S. 💎 Fancy picks!"
                )
            elif choice == "6":
                break
            else:
                print("\n😢 I don't know that command. Please enter a valid option.\n")

        self.db.close()


if __name__ == "__main__":
    tracker = Tracker("db/database.db")
    tracker.run()

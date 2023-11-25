class Syr:
    def user_test(self):
        try:
            # Mapping of months to stores and expenses
            purchases_by_month = {
                "January": {"Zara": 50, "Mercadona": 80, "Asos": 30, "Pharmacy": 12, "Netflix": 11},
                "February": {"IE university": 20, "El Corte Ingles": 200, "Carrefour": 47, "Netflix": 11},
                "March": {"Mercadona": 150, "Decathlon": 90, "Pharmacy": 12, "Netflix": 11},
                "April": {"Zara": 52, "Amazon": 90, "Lidl": 52, "Lateral": 15, "Netflix": 11},
                "May": {"Mercadona": 80, "IE university": 28, "Netflix": 11},
                "June": {"trajesdebaño.com": 45, "Vans": 58, "Rayban": 110, "La Tagliatelle": 22, "Netflix": 11},
                "July": {"Iberia": 654, "Mercadona": 80, "Apple": 1100, "Netflix": 11},
                "August": {"Liberty Club": 30, "Lateral": 87, "Carrefour": 47, "Netflix": 11},
                "September": {"Mercadona": 80, "Zalando": 23, "Pharmacy": 12, "Netflix": 11},
                "October": {"Zara": 52, "GoSushi": 18, "NailsLady": 25, "Netflix": 11},
                "November": {"Mercadona": 80, "Aristocrazy": 53, "Netflix": 11},
                "December": {"Amazon": 47, "Netflix": 11, "Pharmacy": 12, "Netflix": 11}
            }

            # User input for the desired month
            desired_month = input("Question 1: Which month's expenses do you want to see? Enter the month (e.g., November): ").capitalize()

            # Check if the desired month is in the purchases dictionary
            if desired_month in purchases_by_month:
                expenses = purchases_by_month[desired_month]
                print(f"Monthly expenses in {desired_month}:")
                for store, amount in expenses.items():
                    print(f"In {store} he spent around {amount}€")

                # Ask if the user wants to see the annual costs
                show_annual_costs = input("Question 2: Do you want to see the annual costs for each shop? (yes/no): ").lower()
                if show_annual_costs == "yes":
                    # Calculate annual expenses for each shop
                    annual_costs = {store: sum(costs.get(store, 0) for costs in purchases_by_month.values()) for store in set(store for costs in purchases_by_month.values() for store in costs)}

                    # Ask which shop the user wants to see in the annual expenses
                    shop_to_see = input("Question 3: Which shop would you like to see in your annual expense? Enter the shop name: ")
                    if shop_to_see in annual_costs:
                        print(f"Annual expense for {shop_to_see}: {annual_costs[shop_to_see]}€")
                    else:
                        print(f"No data found for {shop_to_see} in annual expenses.")
            else:
                print(f"No expenses found for {desired_month}")

        except Exception as e:
            print(f"Error during user test: {e}")

# Example usage:
syr_app = Syr()
syr_app.user_test()

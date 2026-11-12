import data
from sandwich_maker import SandwichMaker
from cashier import Cashier


# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()




def main():
    while True:
        choice = input("What would you like? (small/ medium/ large/ off/ report): ").lower()

        if choice == "off":
            print("Shutting down...")
            break

        elif choice == "report":
                print(f"Bread: {sandwich_maker_instance.machine_resources['bread']} Slices")
                print(f"Ham: {sandwich_maker_instance.machine_resources['ham']} Slices")
                print(f"Cheese: {sandwich_maker_instance.machine_resources['cheese']} oz")

        elif choice in recipes:
            recipe = recipes[choice]
            if sandwich_maker_instance.check_resources(recipe["ingredients"]):
                coins = cashier_instance.process_coins()
                if cashier_instance.transaction_result(coins, recipe["cost"]):
                    sandwich_maker_instance.make_sandwich(choice, recipe["ingredients"])

if __name__=="__main__":
    main()

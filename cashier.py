class Cashier:
    def __init__(self):
        pass

    def process_coins(self):
        """Returns the total calculated from coins inserted.
        Hint: include input() function here, e.g. input(how many quarters?: )"""
        print("Please insert coins.")
        dollars = int(input("How many large dollars?: "))
        half = int(input("How many half dollars?: "))
        quarters = int(input("How many quarters?: "))
        nickels = int(input("How many nickels?: "))
        total = (dollars + half * .5 + quarters * .25 + nickels * .05)
        return total

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is
        insufficient."""
        if coins >= cost:
            change = round(coins - cost, 2)
            if change > 0:
                print(f"Here is the change: ${change:.2f}")
            return True
        else:
            print("Sorry, the money inserted is not sufficient. Money returned.")
            return False
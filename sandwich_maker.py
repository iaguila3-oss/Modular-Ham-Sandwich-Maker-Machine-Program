
class SandwichMaker:
    def __init__(self, resources):
        self.machine_resources = resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for item in ingredients:
            if ingredients[item] > self.machine_resources[item]:
                print(f"Sorry, {item} is not available.")
                return False
        return True

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Keep count of ingredients used to make sandwich."""
        for item in order_ingredients:
            self.machine_resources[item] -= order_ingredients[item]
        print(f"Your {sandwich_size} sandwich is ready. Enjoy >.<.")
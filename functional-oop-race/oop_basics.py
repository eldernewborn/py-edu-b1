import random


class Apple:
    def __init__(self, color):
        self.color = color
        self.body = 100.0

    def get_bitten(self):
        if self.is_eatable():
            print("Khaaarch")
            self.body = self.body - random.randint(10, 20)

    def is_eatable(self):
        return self.body > 10.0

    def __str__(self):
        return f"I'm a {self.color} apple, and I've got {self.body}% left of me."


my_apple = Apple(color="red")
my_green_apple = Apple(color="green")

print(my_apple)
for i in range(10):
    my_apple.get_bitten()
    print(my_apple)
    if not my_apple.is_eatable():
        print("  Not much left to eat")
        break


# ---------------------------------------------------------
# NOTE: THIS IS A SIMPLE EXAMPLE TO UNDERSTAND CONCEPTS.
# It is intentionally simplified and may NOT be complete
# production-ready Python. Use it to learn classes/objects.
# ---------------------------------------------------------

# -------------------------------
# Python Basics: Classes & Objects
# -------------------------------

# A class is like a "factory" or "blueprint".
# It contains properties (data) and methods (actions).

class Chai:
    # __init__ runs automatically when an object is created
    # 'self' refers to the current object
    def __init__(self, sweetness, milk_level):
        self.sweetness = sweetness   # property of chai
        self.milk_level = milk_level # property of chai

    # Method = function inside a class
    def sip(self):
        print("Sipping chai...")

    def add_sugar(self, amount):
        print(f"Added {amount} sugar.")
        # In a full program you might also update self.sweetness here

# -------------------------------
# Creating an object (instance)
# -------------------------------

# 'my_chai' is an object made from the Chai class
my_chai = Chai(3, 2)  # sweetness = 3, milk_level = 2

# Use methods with dot (.)
my_chai.sip()          # calls sip method
my_chai.add_sugar(2)   # calls add_sugar method


# -------------------------------
# Quick reminders:
# - class -> blueprint
# - __init__ -> setup/initialization method
# - self -> current object reference
# - properties -> data (e.g., sweetness)
# - methods -> actions (e.g., sip, add_sugar)
# - object -> an instance of a class (e.g., my_chai)
# -------------------------------

# Chapter 4: Booleans in Python

# Boolean values
is_boiling = True
print(f"Is boiling? {is_boiling}")

# Boolean as numbers
stir_count = 5
total_actions = stir_count + is_boiling   # True acts as 1
print(f"Total actions: {total_actions}")

# Conversion
milk_present = 0
print(f"Is milk available? {bool(milk_present)}")

milk_present = 1
print(f"Is milk available? {bool(milk_present)}")

milk_present = "Hitesh"
print(f"Is milk available? {bool(milk_present)}")

# Logical operators
water_hot = True
tea_added = False
can_serve_chai = water_hot and tea_added
print(f"Can serve chai? {can_serve_chai}")

tea_added = True
can_serve_chai = water_hot and tea_added
print(f"Can serve chai now? {can_serve_chai}")

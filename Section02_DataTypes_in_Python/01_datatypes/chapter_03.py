# Chapter 3: Integers in Python

# Variables
black_tea_grams = 14
ginger_grams = 3

# Addition
total_grams = black_tea_grams + ginger_grams
print(f"Total grams of tea base: {total_grams}")

# Subtraction
remaining = black_tea_grams - ginger_grams
print(f"Remaining grams of black tea: {remaining}")

# Multiplication
strength = black_tea_grams * 2
print(f"Strength (double the grams): {strength}")

# Division
milk_liters = 7
servings = 4
milk_per_serving = milk_liters / servings
print(f"Milk per serving (true division): {milk_per_serving}")

# Floor Division
total_teabags = 7
pots = 4
bags_per_pot = total_teabags // pots
print(f"Whole tea bags per pot: {bags_per_pot}")

# Modulo
cardamom_pods = 10
pods_per_cup = 3
leftover_pods = cardamom_pods % pods_per_cup
print(f"Leftover cardamom pods: {leftover_pods}")

# Exponentiation
base_strength = 2
scale_factor = 3
flavor_strength = base_strength ** scale_factor
print(f"Scaled flavor strength: {flavor_strength}")

# Readable large numbers
total_leaves = 1_000_000_000
print(f"Total tea leaves harvested: {total_leaves}")


# Notes: Numbers in Python
# 1. Types of Numbers in Python

# Integer (int) → whole numbers without decimals. Example: 10, -42, 0.

# Boolean (bool) → True or False values (internally stored as 1 and 0).

# Floating Point (float) → numbers with decimals (precision matters). Example: 3.14, -0.001.

# Complex (complex) → numbers with real + imaginary part. Example: 2+3j.

# 2. Integers – Basic Operations

# Addition (+) → a + b

# Subtraction (-) → a - b

# Multiplication (*) → a * b

# True Division (/) → always gives decimal (7 / 4 = 1.75)

# Floor Division (//) → ignores decimals (7 // 4 = 1)

# Modulo (%) → remainder of division (10 % 3 = 1)

# Exponentiation (**) → power (2 ** 3 = 8)

# 3. Booleans

# True is treated as 1

# False is treated as 0

# Can be used in math expressions.

# Converted using bool(value):

# bool(0) → False

# bool("") → False

# bool(None) → False

# bool(any_other_value) → True

# Logical Operators

# and → both must be True

# or → at least one must be True

# not → inverts (not True = False)

# 4. Floats

# Used for decimals (3.1415, 1.75).

# Can face precision errors (e.g., 0.1 + 0.2 ≠ 0.3 exactly).

# Use decimal and fractions module for higher precision.

# 5. Complex Numbers

# Written as a + bj (Python uses j instead of i).

# Example: 2 + 3j

# Have .real and .imag attributes.
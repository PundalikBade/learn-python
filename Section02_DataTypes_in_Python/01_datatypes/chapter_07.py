# Chapter 07: Tuples in Python

# Tuples are immutable sequences in Python.
# They are defined using parentheses () and are often used for fixed collections of items.

# Example: Creating a tuple
masala_spices = ("cardamom", "clove", "cinnamon")

print("Main masala spices:", masala_spices)

# -----------------------------------------------------------
# Tuple unpacking
# -----------------------------------------------------------
spice1, spice2, spice3 = masala_spices
print("Unpacked spices:", spice1, spice2, spice3)

# -----------------------------------------------------------
# Using tuples for assignments
# -----------------------------------------------------------
# Example: Ratios while making tea
ginger_ratio, cardamom_ratio = (2, 1)
print("\nInitial Ratio -> Ginger:", ginger_ratio, "Cardamom:", cardamom_ratio)

# Swapping values using tuple unpacking (no third variable needed)
ginger_ratio, cardamom_ratio = cardamom_ratio, ginger_ratio
print("Flipped Ratio -> Ginger:", ginger_ratio, "Cardamom:", cardamom_ratio)

# -----------------------------------------------------------
# Membership testing
# -----------------------------------------------------------
print("\nIs 'ginger' in masala_spices?", "ginger" in masala_spices)
print("Is 'cinnamon' in masala_spices?", "cinnamon" in masala_spices)
print("Is 'Cinnamon' (with capital C) in masala_spices?", "Cinnamon" in masala_spices)


# Chapter 07: Tuples in Python

## What are Tuples?
- Tuples are **immutable** (unchangeable) sequences in Python.
- Defined using **parentheses ()**.
- Can store multiple items of different data types.

Example:
```python
my_tuple = (1, "apple", 3.14)

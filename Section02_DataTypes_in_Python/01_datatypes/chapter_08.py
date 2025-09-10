# Chapter 08: Lists in Python

# Lists are mutable sequences in Python.
# That means you can change them (add, remove, update elements).

# Example: Creating a list
ingredients = ["water", "milk", "black tea"]
print("Initial ingredients:", ingredients)

# -----------------------------------------------------------
# Append (add element at the end)
# -----------------------------------------------------------
ingredients.append("sugar")
print("After adding sugar:", ingredients)

# -----------------------------------------------------------
# Remove (delete specific element by value)
# -----------------------------------------------------------
ingredients.remove("water")
print("After removing water:", ingredients)

# -----------------------------------------------------------
# Extend (merge two lists)
# -----------------------------------------------------------
spice_options = ["ginger", "cardamom"]
chai_ingredients = ["water", "milk"]

chai_ingredients.extend(spice_options)
print("\nChai ingredients after extending:", chai_ingredients)

# -----------------------------------------------------------
# Insert (add element at a specific index)
# -----------------------------------------------------------
chai_ingredients.insert(2, "black tea")
print("Chai ingredients after inserting black tea at index 2:", chai_ingredients)

# -----------------------------------------------------------
# Pop (remove and return last element)
# -----------------------------------------------------------
last_added = chai_ingredients.pop()
print("Last removed item:", last_added)
print("Chai ingredients after pop:", chai_ingredients)

# -----------------------------------------------------------
# Reverse (reverse the entire list)
# -----------------------------------------------------------
chai_ingredients.reverse()
print("Reversed chai ingredients:", chai_ingredients)

# -----------------------------------------------------------
# Sort (alphabetically or numerically)
# -----------------------------------------------------------
chai_ingredients.sort()
print("Sorted chai ingredients:", chai_ingredients)

# -----------------------------------------------------------
# Using max() and min() with lists
# -----------------------------------------------------------
sugar_levels = [1, 2, 3, 4, 5]
print("\nMaximum sugar level:", max(sugar_levels))
print("Minimum sugar level:", min(sugar_levels))

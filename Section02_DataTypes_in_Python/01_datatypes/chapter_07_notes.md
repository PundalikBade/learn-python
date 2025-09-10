# Chapter 07: Tuples in Python

## What are Tuples?
- Tuples are **immutable** (unchangeable) sequences in Python.
- Defined using **parentheses ()**.
- Can store multiple items of different data types.

Example:
```python
my_tuple = (1, "apple", 3.14)


Key Features

Immutable

Once created, elements cannot be changed.

Tuple Unpacking

Assign tuple values directly to variables:

a, b, c = (10, 20, 30)


Swapping Variables

Swap values without a temporary variable:

x, y = 5, 10
x, y = y, x


Membership Test

Check if an item exists in a tuple using in:

"apple" in my_tuple  # True

Why Use Tuples?

Faster than lists (performance benefit).

Good for fixed data that shouldn’t change.

Commonly used in function returns (returning multiple values).
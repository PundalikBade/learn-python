# Chapter 5: Floating Point Numbers in Python

# Floating point numbers
ideal_temp = 95.5
current_temp = 95.49999999
diff_temp = ideal_temp - current_temp

print(f"Ideal temperature: {ideal_temp}")
print(f"Current temperature: {current_temp}")
print(f"Difference: {diff_temp}")

# Precision info
import sys
print("Float info:", sys.float_info)

# Fractions
from fractions import Fraction
print("Fraction example:", Fraction(3, 7))

# Decimal for precision
from decimal import Decimal
value = Decimal("0.1") + Decimal("0.2")
print("Using Decimal (0.1 + 0.2):", value)

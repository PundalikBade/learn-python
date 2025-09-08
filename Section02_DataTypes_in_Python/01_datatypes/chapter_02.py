# spice_mix = set()
# print(f"Initial spice mix id:{id(spice_mix)}")
# spice_mix.add("Ginder")

# spice_mix.add("cardmom")
# spice_mix.add("lemon")

# print(f"Initial spice mix id:{id(spice_mix)}")

# print(f"Initial spice mix id:{id(spice_mix)}")

# List is mutable
# nums = [1, 2, 3]
# nums[0] = 99       # change element
# nums.append(4)     # add element
# print(nums)        # [99, 2, 3, 4]


# String is immutable
# name = "python"
# name = name.upper()  # creates a new string
# print(name)              # "python"
#           # "PYTHON"

a = [1, 2, 3]
b = a
a[0] = 99
print(a)  # [99, 2, 3]
print(b)  # [99, 2, 3]  (changed too!)

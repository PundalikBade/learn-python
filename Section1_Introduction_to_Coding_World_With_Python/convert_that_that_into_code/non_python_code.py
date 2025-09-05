# --------------------------------------------------------
# NOTE: This is NOT correct Python code.
# It is written in Python-like style to explain the steps
# of making chai (tea) in a beginner-friendly way.
#
# The functions used here (like kettle_has_water, fill_kettle, etc.)
# are NOT real Python functions. They are just placeholders.
# You would need to define them (e.g., with print statements)
# if you want to run this program.
#
# Purpose: Documentation / pseudo-code for understanding logic
# --------------------------------------------------------

def make_chai():
    # Step 1: Check if the kettle has water
    if not kettle_has_water():
        fill_kettle()          # Fill the kettle with water
        plug_in_kettle()       # Plug in the kettle
        boil_water()           # Boil the water

    # Step 2: Check if the cup is clean
    if not is_cup_clean():
        wash_cup()             # Wash the cup if it is dirty

    # Step 3: Add ingredients to the cup
    add_to_cup("tea_leaves")   # Add tea leaves
    add_to_cup("sugar")        # Add sugar

    # Step 4: Pour the boiled water into the cup
    pour("boiled water")

    # Step 5: Stir the cup
    stir("cup")

    # Step 6: Serve the chai
    serve("chai")

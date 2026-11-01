
# Lab 10 - Python Lists and Tuples
#
# Reflection 1:
# The most surprising thing to me was how Python lists start
# counting at zero instead of one. I also thought it was
# interesting how you can use negative numbers to get items
# from the end of a list.
#
# Reflection 2:
# When I was making speaker pods and walls for my small business,
# I had to keep track of different materials and prices.
# Using Python lists could have saved me time by automatically
# calculating totals and organizing the prices instead of
# manually doing everything in Excel.


# Exercise 1 - Build the list
inventory = ["pen", "notebook", "stapler", "tape", "marker"]

print("Exercise 1:")
print(inventory)
print(len(inventory))


# Exercise 2 - Index practice
print("\nExercise 2:")
print(inventory[0])
print(inventory[-1])
print(inventory[len(inventory) // 2])


# Exercise 3 - Slicing
print("\nExercise 3:")
print(inventory[:3])
print(inventory[-2:])
print(inventory[::2])


# Exercise 4 - Modify
print("\nExercise 4:")
inventory.append("envelope")
print(inventory)

inventory.remove("tape")
print(inventory)

inventory.sort()
print(inventory)


# Exercise 5 - Tuple comparison
print("\nExercise 5:")
coords = (40.7128, -74.0060)

try:
    coords[0] = 99
except TypeError:
    print("TypeError caught")
    print("Tuples are useful for coordinates because they cannot be changed.")

print(coords)


# Exercise 6 - Average of a list of sales
print("\nExercise 6:")
sales = [100, 250, 75, 480, 200]

total = sum(sales)
count = len(sales)
average = total / count

print("Total:", total)
print("Count:", count)
print("Average:", average)
print("Best:", max(sales))
print("Worst:", min(sales))


# Exercise 7 - Accumulator pattern
print("\nExercise 7:")
prices = [9.99, 14.99, 4.99, 24.99, 1.99]
discounted = []

for price in prices:
    new_price = round(price * 0.90, 2)
    discounted.append(new_price)

print("Original:", prices)
print("Discounted:", discounted)


# Exercise 8 - Filter above threshold
print("\nExercise 8:")
sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]

high_sales = []

for sale in sales:
    if sale > 300:
        high_sales.append(sale)

print(high_sales)
print("Count:", len(high_sales))
print("Average:", round(sum(high_sales) / len(high_sales), 2))

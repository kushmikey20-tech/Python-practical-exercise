Asking the user for inputs (initially strings)
raw_age = input("Enter your age: ")
raw_height = input("Enter your height (in meters): ")
raw_weight = input("Enter your weight (in kg): ")

Converting values to appropriate numeric types
age = int(raw_age)
height = float(raw_height)
weight = float(raw_weight)

Displaying their data types using type()
print("\n--- Converted Data Types ---")
print(f"Age: {age}, Type: {type(age)}")
print(f"Height: {height}, Type: {type(height)}")
print(f"Weight: {weight}, Type: {type(weight)}")
Getting input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

Calculating operations
total_sum = num1 + num2
difference = num1 - num2
product = num1 * num2
quotient = num1 / num2 if num2 != 0 else "Undefined (division by zero)"
remainder = num1 % num2 if num2 != 0 else "Undefined"
power = num1 ** num2

Displaying results
print("\n--- Calculator Results ---")
print(f"Sum: {total_sum}")
print(f"Difference: {difference}")
print(f"Product: {product}")
print(f"Quotient: {quotient}")
print(f"Remainder: {remainder}")
print(f"First number raised to the power of the second: {power}")
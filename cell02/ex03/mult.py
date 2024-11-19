first_number = int(input("Enter the first number:\n"))
second_number = int(input("Enter the second number:\n"))
product = first_number * second_number

print(f"{first_number} x {second_number} = {product}")

if product < 0:
    print("The result is negative.")
elif product > 0:
    print("The result is positive.")
else:
    print("The result is positive and negative.")
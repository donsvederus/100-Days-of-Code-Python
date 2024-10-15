# Function to determine if a number is even or odd
def determine_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Example usage
number = int(input("Enter a number: "))
result = determine_even_odd(number)
print(f"The number {number} is {result}.")
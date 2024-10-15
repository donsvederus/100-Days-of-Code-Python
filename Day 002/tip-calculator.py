# Step 1: Ask for the number of people
num_people = int(input("Enter the number of people: "))

# Step 2: Ask for the total bill amount
total_bill = float(input("Enter the total bill amount: "))

# Step 3: Ask for the tip percentage
tip_percentage = float(input("Enter the tip percentage: "))

# Step 4: Calculate the total tip amount
total_tip = total_bill * (tip_percentage / 100)

# Step 5: Calculate the total bill including the tip
total_bill_with_tip = total_bill + total_tip

# Step 6: Calculate the amount each person should pay
amount_per_person = total_bill_with_tip / num_people

# Step 7: Round the result to the nearest cent
amount_per_person = round(amount_per_person, 2)

# Step 8: Print the result
print(f"Each person should pay: ${amount_per_person}")
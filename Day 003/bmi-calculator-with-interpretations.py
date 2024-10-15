height = 1.65 
weight = 60

# Calculate the bmi using weight and height.
bmi = weight / (height ** 2)

# Round the BMI to 2 decimal places
bmi = round(bmi, 2)

# Print the BMI value
print(f"BMI: {bmi}")

# Interpret the BMI value
if bmi < 18.5:
    print("underweight")
elif 18.5 <= bmi < 25:
    print("normal weight")
else:
    print("overweight")
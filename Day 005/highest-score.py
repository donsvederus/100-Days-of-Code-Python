student_scores = [85, 92, 78, 64, 88, 91, 73, 95, 67, 82, 76, 89, 94, 58, 99, 81, 77, 69, 84, 90]

# Initialize a variable to store the highest score
highest_score = 0

# Iterate through each score in the list
for score in student_scores:
    # If the current score is higher than the highest score, update the highest score
    if score > highest_score:
        highest_score = score

# Print the highest score
print(f"The highest score is: {highest_score}")
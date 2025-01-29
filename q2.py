# Make a random pet.
import random

# Choose:
# Type of animal (at least 3 choices, string)
animal = random.choice(["dog", "cat", "horse", "parrot", "giraffe", "hippo"])
# Age (integer)
age = random.randint(1, 100)
# Color (at least 3 choices, string)
color = random.choice(["black", "brown", "grey", "white", "red", "orange", "yellow", "green", "blue", "purple", "pink"])
# Weight (float)
weight = random.uniform(1, 8000)

# Print a summary of your pet using an f-string
print(f"Your pet is a {age}-year-old, {color} {animal}, who weighs {weight} pounds!")
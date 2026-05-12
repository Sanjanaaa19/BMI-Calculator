# BMI Calculator in Python

print("=== BMI Calculator ===")

# Taking input from the user
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

# Calculating BMI
bmi = weight / (height ** 2)

# Displaying BMI Value
print(f"\nYour BMI is: {bmi:.2f}")

# Checking BMI Category
if bmi < 18.5:
    print("Category: Underweight")
elif 18.5 <= bmi < 24.9:
    print("Category: Normal weight")
elif 25 <= bmi < 29.9:
    print("Category: Overweight")
    
else:
    print("Category: Obese")

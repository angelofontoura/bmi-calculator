# bmi_calculator.py - Initial version
def calculate_bmi(weight, height):
    return weight / (height ** 2)

def classify_bmi(bmi):
    if bmi < 18.5: return "Underweight"
    if bmi < 25: return "Normal weight"
    if bmi < 30: return "Overweight"
    if bmi < 35: return "Obesity class I"
    if bmi < 40: return "Obesity class II"
    return "Obesity class III"

# Example 
weight = 70  # kg
height = 1.75  # meters

bmi = calculate_bmi(weight, height)
classification = classify_bmi(bmi)

print(f"BMI: {bmi:.2f} - {classification}")
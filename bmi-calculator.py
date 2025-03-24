# bmi_calculator.py - Version with user interaction
def calculate_bmi(weight, height):
    return weight / (height ** 2)  # Correct calculation

def classify_bmi(bmi):
    if bmi < 18.5: return "Underweight"
    if bmi < 25: return "Normal weight"
    if bmi < 30: return "Overweight"
    if bmi < 35: return "Obesity class I"
    if bmi < 40: return "Obesity class II"
    return "Obesity class III"

def main():
    print("\nBMI Calculator\n")
    try:
        weight = float(input("Enter your weight in kg: "))
        height = float(input("Enter your height in meters: "))
        
        bmi = calculate_bmi(weight, height)
        classification = classify_bmi(bmi)
        
        print(f"\nYour BMI is: {bmi:.2f}")
        print(f"Classification: {classification}\n")
    except ValueError:
        print("\nError: Please enter valid numbers\n")

if __name__ == "__main__":
    main()
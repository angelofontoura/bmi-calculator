def calculate_bmi(weight, height):
    """Calculate BMI from weight (kg) and height (m).
    Args:
        weight: float (weight in kilograms)
        height: float (height in meters)
    Returns:
        float: BMI value
    """
    return weight / (height ** 2)

def classify_bmi(bmi):
    """Classify BMI into health categories.
    Args:
        bmi: float
    Returns:
        str: Health classification
    """
    if bmi < 18.5: return "Underweight"
    if bmi < 25: return "Normal weight"
    if bmi < 30: return "Overweight"
    if bmi < 35: return "Obesity class I"
    if bmi < 40: return "Obesity class II"
    return "Obesity class III"

def get_valid_input(prompt, min_val, max_val):
    """Get and validate user input.
    Args:
        prompt: str - Display text
        min_val: float - Minimum allowed value
        max_val: float - Maximum allowed value
    Returns:
        float: Validated input
    """
    while True:
        try:
            value = float(input(prompt))
            if min_val <= value <= max_val:
                return value
            print(f"Error: Value must be between {min_val} and {max_val}.")
        except ValueError:
            print("Error: Please enter a valid number.")

def main():
    """Main program execution."""
    print("\nBMI Calculator\n")
    weight = get_valid_input("Enter weight (kg): ", 10, 300)  # 10kg to 300kg
    height = get_valid_input("Enter height (m): ", 0.5, 2.5)   # 0.5m to 2.5m
    
    bmi = calculate_bmi(weight, height)
    classification = classify_bmi(bmi)
    
    print(f"\nYour BMI is: {bmi:.2f}")
    print(f"Classification: {classification}\n")

if __name__ == "__main__":
    main()
import pytest
from bmi_calculator import calculate_bmi, classify_bmi

def test_calculate_bmi():
    assert calculate_bmi(70, 1.75) == pytest.approx(22.86, 0.01)

def test_classify_bmi():
    assert classify_bmi(18.4) == "Underweight"
    assert classify_bmi(24.9) == "Normal weight"


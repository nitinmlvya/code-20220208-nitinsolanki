import pytest
from app.app import BMICalculator


def test_calculate_bmi():
	bmi = BMICalculator().calculate_bmi(weight_in_kg=75, height_in_cm=175)
	assert bmi == 24.49


def test_health_risk_and_bmi_category():
	health_risk, bmi_category = BMICalculator().get_health_risk_and_bmi_category(bmi=24.49)
	assert health_risk == 'Low risk'
	assert bmi_category == 'Normal weight'


def test_result():
	person_data = [{"Gender": "Male", "HeightCm": 175, "WeightKg": 75 }]
	person = person_data[0]
	calc = BMICalculator()
	bmi = calc.calculate_bmi(person['WeightKg'], person['HeightCm'])
	health_risk, bmi_category = calc.get_health_risk_and_bmi_category(bmi=bmi)

	assert bmi == 24.49
	assert health_risk == 'Low risk'
	assert bmi_category == 'Normal weight'

import time
import json
import pandas as pd
from typing import List, Dict, Tuple
from tqdm import tqdm
from flask import Flask

app = Flask(__name__)


health_risk_bmi_data = {
	"BMI_category": ["Underweight", "Normal weight", "Overweight", "Moderately obese", "Severely obese", "Very severely obese"],
	"BMI_range": [(None, 18.4), (18.4, 24.9), (24.9, 29.9), (29.9, 34.9), (34.9, 39.9), (39.9, None)],
	"health_risk": ["Malnutrition risk", "Low risk", "Enhanced risk", "Medium risk", "High risk", "Very high risk"]
}



class BMICalculator():
	def __init__(self) -> None:
		self.input_json_file = 'test_data.json'
		self.output_csv_file = 'test_output.csv'

		self.person_bmi_details = {'BMI': [], 'health_risk': [], 'BMI_category': []}
		self.overweight_persons_count = 0


	def __convert_to_meter(self, value: float) -> float:
		"""
		Method to convert centimeter to meter
		"""
		return value * 0.01


	def calculate_bmi(self, weight_in_kg: int, height_in_cm: int) -> float:
		"""
		Method to calcuate the BMI value based on weight & height.
		"""
		height_in_m = self.__convert_to_meter(height_in_cm)
		bmi = weight_in_kg / (height_in_m * height_in_m)
		return round(bmi, 2)


	def get_health_risk_and_bmi_category(self, bmi: float) -> Tuple[str, str]:
		"""
		Method to retrieve the health risk & BMI category based on BMI value.

		"""
		list_of_bmi_range = health_risk_bmi_data['BMI_range']
		for i, bmi_range in enumerate(list_of_bmi_range):
			if i == 0:
				if bmi <= bmi_range[1]:
					return health_risk_bmi_data['health_risk'][i], health_risk_bmi_data['BMI_category'][i]
			elif i == len(list_of_bmi_range)-1:
				if bmi > bmi_range[0]:
					return health_risk_bmi_data['health_risk'][i], health_risk_bmi_data['BMI_category'][i]
			else:
				if bmi > bmi_range[0] and bmi <= bmi_range[1]:
					return health_risk_bmi_data['health_risk'][i], health_risk_bmi_data['BMI_category'][i]


	def save_details(self):
		df = pd.DataFrame(self.person_bmi_details)
		df.to_csv(self.output_csv_file, index=False)
		print(f'Output saved to file : {self.output_csv_file}')


	def run(self) -> None:
		"""
		Main method to run the program and count the overweighted persons.
		"""
		print(f'Reading person details from file: {self.input_json_file}')
		data_json = json.load(open(self.input_json_file))

		for person in tqdm(data_json, desc ="Calculating BMI..."):
			bmi = self.calculate_bmi(person['WeightKg'], person['HeightCm'])
			health_risk, bmi_category = self.get_health_risk_and_bmi_category(bmi)

			self.person_bmi_details['BMI'].append(bmi)
			self.person_bmi_details['health_risk'].append(health_risk)
			self.person_bmi_details['BMI_category'].append(bmi_category)

			if bmi_category == health_risk_bmi_data['BMI_category'][2]:
				self.overweight_persons_count += 1

		self.save_details()


@app.route('/', methods = ['POST'])
def hello_world():
	calc = BMICalculator()
	calc.run()
	return str(calc.overweight_persons_count)



if __name__=='__main__':
	app.run()
	# BMICalculator().run()
	




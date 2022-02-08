data = [{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 }, { "Gender": "Male", "HeightCm": 161, "WeightKg": 85 }, { "Gender": "Male", "HeightCm": 180, "WeightKg": 77 }, { "Gender": "Female", "HeightCm": 166, "WeightKg": 62}, {"Gender": "Female", "HeightCm": 150, "WeightKg": 70}, {"Gender": "Female", "HeightCm": 167, "WeightKg": 82}]

health_risk_bmi_data = {
	"BMI_category": ["Underweight", "Normal weight", "Overweight", "Moderately obese", "Severely obese", "Very severely obese"],
	"BMI_range": [(None, 18.4), (18.4, 24.9), (24.9, 29.9), (29.9, 34.9), (34.9, 39.9), (39.9, None)],
	"health_risk": ["Malnutrition risk", "Low risk", "Enhanced risk", "Medium risk", "High risk", "Very high risk"]
}


class Solution():
	def __init__(self):
		self.overweight_persons_count = 0

	def __convert_to_meter(self, value):
		return value * 0.01


	def calculate_bmi(self, weight_in_kg, height_in_cm):
		height_in_m = self.__convert_to_meter(height_in_cm)
		bmi = weight_in_kg / (height_in_m * height_in_m)
		return round(bmi, 2)


	def calcuate_health_risk(self, bmi):
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

	def run(self, weight_in_kg=75, height_in_cm=175):
		bmi = self.calculate_bmi(weight_in_kg, height_in_cm)
		health_risk, bmi_category = self.calcuate_health_risk(bmi)
		if bmi_category == health_risk_bmi_data['BMI_category'][2]:
			self.overweight_persons_count += 1
		print(f'BMI: {bmi} & Health Risk: {health_risk}, & BMI Category: {bmi_category}')

if __name__=='__main__':
	# Solution().run()
	sol = Solution()
	for person in data:
		sol.run(weight_in_kg=person['WeightKg'], height_in_cm=person['HeightCm'])
		print()
	print(f'Overweight Persons: {sol.overweight_persons_count}')
	



import json
from flask import Flask
from flask import request
from bmi_calculator import BMICalculator


app = Flask(__name__)


@app.route('/process', methods = ['POST'])
def bmi_service():
	print(f'Reading person details from file...')
	file_ = request.files['input_data']
	data_json = json.load(file_)
	calc = BMICalculator()
	calc.run(data_json)
	return {'overweight_persons_count': calc.overweight_persons_count, 'result': calc.person_bmi_details} 


@app.route('/health_check', methods = ['GET'])
def health_check():
	return 'health check is done.'


@app.route('/', methods = ['GET'])
def welcome():
	return 'Welcome to BMI Calculator...'


if __name__=='__main__':
	app.run()
	# BMICalculator().run()
	




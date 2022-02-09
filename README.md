# code-20220208-nitinsolanki

## Prerequisite 
- Python >= 3.6 Version

## Github code link
https://github.com/nitinmlvya/code-20220208-nitinsolanki

## Hosting/deployment link
https://code-20220208-nitinsolanki.herokuapp.com


### Steps of CI/CD deployment:
- Code is hosted on github.
- Push the recent changes to "master" branch. It automatically executes the CI pipeline with Github Actions, installs the necessary python packages, makes the build and executes the unit test cases.
- Once the github build and tests are executed successfully, it triggers the CD pipeline hosted over Heroku.
- Heroku automatically picks the latest commit of the "master" branch from the github and executes the build.
- Once the build will get completed, it deploys the code to URL - https://code-20220208-nitinsolanki.herokuapp.com
- Check Endpoint to test the application.


### Endpoint / API hosted on heroku

curl --location --request POST 'https://code-20220208-nitinsolanki.herokuapp.com/process' \
--form 'input_data=@"/Users/nitinsolanki/Documents/code_mania/assignments/code-20220208-nitinsolanki/input/test_data.json"'


### Test the API locally

- Run the command "python app.py"

- Test the below API
curl --location --request POST 'http://127.0.0.1:5000/process' \
--form 'input_data=@"/Users/nitinsolanki/Documents/code_mania/assignments/code-20220208-nitinsolanki/input//test_data.json"'


**NOTE: Make sure to change the input json file path.**


## Request & Response.

### Request
- Provide the JSON file to "input_data" parameter in the request body. (For test purpose, you can find two JSON files into the "input" directory of the code.)

### Response:


{
    "overweight_persons_count": 1,  ## Counts the overweighted persons.
    "result": [  					## result has the said BMI output for the given json file.
        {
            "BMI": 32.83,
            "BMI_category": "Moderately obese",
            "health_risk": "Medium risk"
        },
        {
            "BMI": 32.79,
            "BMI_category": "Moderately obese",
            "health_risk": "Medium risk"
        },
        {
            "BMI": 23.77,
            "BMI_category": "Normal weight",
            "health_risk": "Low risk"
        },
        {
            "BMI": 22.5,
            "BMI_category": "Normal weight",
            "health_risk": "Low risk"
        },
        {
            "BMI": 31.11,
            "BMI_category": "Moderately obese",
            "health_risk": "Medium risk"
        },
        {
            "BMI": 29.4,
            "BMI_category": "Overweight",
            "health_risk": "Enhanced risk"
        }
    ]
}





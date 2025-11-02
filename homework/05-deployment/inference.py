import requests

sample = {
    "lead_source": "organic_search",
    "number_of_courses_viewed": 4,
    "annual_income": 80304.0
}

# sample =  {
#     "lead_source": "paid_ads",
#     "number_of_courses_viewed": 2,
#     "annual_income": 79276.0
# }

url = "http://0.0.0.0:8000/predict"

response = requests.post(url, json=sample)

predict = response.json()

print(predict)
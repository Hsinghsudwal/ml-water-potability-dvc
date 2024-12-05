import requests


url = 'http://localhost:9696/predict'

sample = {
    "ph":9.092223,
    "Hardness":181.101509,
    "Solids":17978.986339,
    "Chloramines":6.546600,
    "Sulfate":310.135738,
    "Conductivity":398.410813,
    "Organic_carbon":11.558279,
    "Trihalomethanes":31.997993,
    "Turbidity":4.075075
    }

response = requests.post(url, json=sample).json()
print(response)
# 0
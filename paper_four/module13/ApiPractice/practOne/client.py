import requests

BASE = "http://127.0.0.1:8000"

response = requests.get(f"{BASE}/")
print(response.status_code)
print(response.headers["content-Type"])
print(response.json())

response = requests.get(f"{BASE}/welcome", params={"name" : "Abi"})
print(response.url)
print(response.json())

house = {"area_sqft": 1500, "bedrooms": 3, "bathrooms": 2, "age_years": 5, "distance_city_km": 8.5}
response = requests.post(f"{BASE}/predict", json=house)
print(response.status_code, response.json())

bad = {**house, "area_sqft" : "abc"}
print(requests.post(f"{BASE}/predict", json=bad).status_code)
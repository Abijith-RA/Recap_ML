"""step2_client.py - Topic 2: call the API like a real client. Start step2_server.py first."""
import requests

BASE = "http://127.0.0.1:8000"

# GET: read status code, headers and the JSON body
response = requests.get(f"{BASE}/")
print(response.status_code)                    # 200 = success
print(response.headers["Content-Type"])        # application/json
print(response.json())                         # the JSON body as a Python dict

# GET with a query parameter
response = requests.get(f"{BASE}/welcome", params={"name": "Asha"})
print(response.url)                            # .../welcome?name=Asha
print(response.json())

# POST with a JSON body
house = {"area_sqft": 1500, "bedrooms": 3, "bathrooms": 2, "age_years": 5, "distance_city_km": 8.5}
response = requests.post(f"{BASE}/predict", json=house)
print(response.status_code, response.json())

# Bad input: the server answers with a 4xx code (422 = invalid data)
bad = {**house, "area_sqft": "abc"}
print(requests.post(f"{BASE}/predict", json=bad).status_code)

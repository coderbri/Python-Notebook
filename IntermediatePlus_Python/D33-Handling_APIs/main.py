import requests

# 1. Send a GET request to the ISS location endpoint
response = requests.get(url="http://api.open-notify.org/iss-now.json")

# Output raw response object and raw status integer code (e.g., 200)
print(response)
print(response.status_code)

# 2. Check for HTTP errors; raises an exception automatically if code is 4xx or 5xx
response.raise_for_status()
# if response.status_code == 400:
#     raise Exception("That resource does not exist.")
# elif response.status_code == 401:
#     raise Exception("You are not authorized to access this data.")

# 3. Parse JSON body from the response into a Python dictionary
data = response.json()
print(data)

iss_position_data = response.json()["iss_position"]
print(iss_position_data)

iss_latitude_data = response.json()["iss_position"]["latitude"]
print(iss_latitude_data)

# 4. Extract nested values from the dictionary
# Structure: {"iss_position": {"latitude": "...", "longitude": "..."}}
longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

# 5. Store geographic coordinates in a tuple for quick reference
iss_position = (longitude, latitude)
print(f"Current ISS position: {iss_position}")

import pandas as pd
import requests
import openpyxl
import sqlite3
# Function to get weather data from OpenWeatherMap API
def get_weather_data(latitude, longitude, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Error fetching weather data.")
        return None

# Read Excel file
excel_file = "D:\\Arslan testing Data\\file.xlsx"  # Path to your Excel file
df = pd.read_excel(excel_file)

# Iterate over rows and get weather data for each location
api_key = "2da748067a01be6fda9d14751cfe9d29"
for index, row in df.iterrows():
    latitude = row['lat']
    longitude = row['lon']
    print(f"Getting weather data for latitude: {latitude}, longitude: {longitude}")
    weather_data = get_weather_data(latitude, longitude, api_key)
    if weather_data:
        weather_id = weather_data['weather'][0]['id']  # Extract weather ID from the response
        print(f"Weather ID: {weather_id}")
#Note: The final script will NOT be AI Generated. This is just an AI generated concept.
import network
import socket
import time
import json
from pimoroni import UnicornPack

# Initialize Unicorn Pack
unicorn = UnicornPack()

# Set up Wi-Fi
def connect_wifi(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)

    while not wlan.isconnected():
        time.sleep(1)

    print("Connected to Wi-Fi:", wlan.ifconfig())

# Fetch weather data from Open-Meteo
def fetch_weather(latitude, longitude):
    url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={latitude}&longitude={longitude}&"
        f"current_weather=true&"
        f"hourly=temperature_2m,relative_humidity_2m,apparent_temperature,precipitation_probability,wind_speed_10m&"
        f"daily=sunrise,sunset,daylight_duration&"
        f"timezone=America/New_York"
    )
    addr = socket.getaddrinfo("api.open-meteo.com", 80)[0][-1]

    s = socket.socket()
    s.connect(addr)
    s.send(b"GET " + url.encode() + b" HTTP/1.0\r\nHost: api.open-meteo.com\r\n\r\n")

    response = s.recv(2048)  # Increased buffer size for larger responses
    s.close()

    # Parse JSON response
    data = json.loads(response.split(b'\r\n\r\n')[1])
    return data

# Example usage
ssid = "your_wifi_ssid"
password = "your_wifi_password"
latitude = your_latitude  # e.g., 40.7128 for New York
longitude = your_longitude  # e.g., -74.0060 for New York

connect_wifi(ssid, password)
weather_data = fetch_weather(latitude, longitude)

# Accessing current weather
current_weather = weather_data['current_weather']
print("Current Weather:", current_weather)

# Displaying current weather information
temperature = current_weather['temperature']
wind_speed = current_weather['windspeed']
is_day = current_weather['is_day']

# Update Unicorn Pack with weather data
if is_day:
    unicorn.set_all(255, 255, 0)  # Yellow for daytime
else:
    unicorn.set_all(0, 0, 255)     # Blue for nighttime
unicorn.show()

# Additional logic for displaying temperature and wind speed can be added here

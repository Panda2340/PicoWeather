#Note: The final script will NOT be AI Generated. This is just an AI generated concept.
import network
import socket
import time
import json
import machine
from pimoroni import UnicornHat

# Initialize Unicorn HAT
unicorn = UnicornHat()

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
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
    addr = socket.getaddrinfo("api.open-meteo.com", 80)[0][-1]

    s = socket.socket()
    s.connect(addr)
    s.send(b"GET " + url.encode() + b" HTTP/1.0\r\nHost: api.open-meteo.com\r\n\r\n")

    response = s.recv(1024)
    s.close()

    # Parse JSON response
    data = json.loads(response.split(b'\r\n\r\n')[1])
    return data['current_weather']

# Example usage
ssid = "your_wifi_ssid"
password = "your_wifi_password"
latitude = your_latitude
longitude = your_longitude

connect_wifi(ssid, password)
weather = fetch_weather(latitude, longitude)
print("Current Weather:", weather)

# Update Unicorn HAT with weather data
# Example: you can set colors based on temperature

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
from datetime import datetime
import time
import urllib.request
import json
import requests

# Define the URL to get the current location of the ISS
url = 'http://api.open-notify.org/iss-now.json'

# Create a Basemap object
m = Basemap(projection='merc', llcrnrlat=-80, urcrnrlat=80,
            llcrnrlon=-180, urcrnrlon=180, lat_ts=20, resolution='c')

# Draw coastlines, countries, and boundaries
m.drawcoastlines()
m.drawcountries()
m.drawmapboundary()

# Make a request to the Open Notify API to get the current location of the ISS
response = requests.get("http://api.open-notify.org/iss-now.json")

# Parse the JSON response to get the latitude and longitude of the ISS
iss_position = response.json()["iss_position"]
latitude = iss_position["latitude"]
longitude = iss_position["longitude"]

# Use the OpenCage Geocoder API to get the name of the location where the ISS is currently located
opencage_api_key = "YOUR_OPENCAGE_API_KEY_HERE" # Replace with your own OpenCage API key
opencage_url = f"https://api.opencagedata.com/geocode/v1/json?q={latitude}+{longitude}&key={opencage_api_key}"
opencage_response = requests.get(opencage_url)
location_name = opencage_response.json()["results"][0]["formatted"]



# Continuously update the map with the current location of the ISS
while True:
    # Get the current location of the ISS
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())
    iss_lat = float(data['iss_position']['latitude'])
    iss_lon = float(data['iss_position']['longitude'])

    # Convert the latitude and longitude to x and y coordinates
    x, y = m(iss_lon, iss_lat)

    # Clear the previous plot and plot a red dot on the map at the current location of the ISS
    plt.clf()
    m.drawcoastlines()
    m.drawcountries()
    m.drawmapboundary()
    m.plot(x, y, 'ro', markersize=10)
    
    # Add the current time to the plot title
    plt.title(f"Current Location of the ISS as of : { datetime.now().strftime('%Y-%m-%d %H:%M:%S')} Location : {location_name} ")

    # Display the plot and pause for 1 second
    plt.show(block=False)
    plt.pause(1)

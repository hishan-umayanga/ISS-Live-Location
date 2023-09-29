# ISS-Live-Location
 ISS LIVE
 



To run the above code, you will need to install the :-

      requests ( pip install requests)
      
      This will download and install the requests library and its dependencies,
      which should allow you to import and use it in your Python code. Once the library is 
      installed, you can import it in your code using the import requests statement.
      
      
      basemap  ( pip install basemap)
      
Use the OpenCage Geocoder API to get the name of the location where the ISS is currently located.

 Make sure to replace "YOUR_OPENCAGE_API_KEY_HERE" with your actual OpenCage API key. 
 
 You can sign up for a free API key at https://opencagedata.com/


used the requests library to retrieve the current location of the International Space Station from the Open Notify API, and parse the JSON response using the json library.   
      
use the Basemap library to plot the current location of the ISS on a world map.   



To get the current latitude and longitude of the ISS from the URL http://api.open-notify.org/iss-now.json.The while loop continuously updates the map with the current location of the ISS.

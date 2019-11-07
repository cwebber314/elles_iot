"""
Mock IOT which sends data to the raspberry pi.  

Doing this as a GET probably violates the REST guidelines, but I suspect it's easier than 
encoding the data in request body. 
"""
import requests
import time

for i in range(1000):
    # Params is for GET style URL parameters
    # data is for putting data in the body  
    requests.get('http://localhost:8001/position', params={'position': i, 'comment': 'Shop smart, shop s-mart'})
    time.sleep(0.3)
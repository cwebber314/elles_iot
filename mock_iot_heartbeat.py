"""
Mock IOT which gets data from the raspberry pi.
"""
import requests
import time

for i in range(100):
    requests.get('http://localhost:8001/heartbeat')
    time.sleep(0.3)
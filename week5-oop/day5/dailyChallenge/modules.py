import requests
import time 
def calculete_response_time(url):
    startTIme = time.time()
    resopnse = requests.get(url)
    endTime = time.time()

    resopnseTime = endTime -startTIme
    return resopnseTime

responseTime=calculete_response_time("www.google.com")

print(responseTime) # Outputs the response time in seconds


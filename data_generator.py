import random
import time
import requests

from services.VikingService import VikingService


def getTimeEpoch():
    return time.time()


def getRandomFloat():
    return random.randrange(20.0, 22.0)


timeInSeconds = 86400 * 30
epochTime = getTimeEpoch()
startTime = epochTime - timeInSeconds

viking = VikingService()

full_data = {
    "data": []
}

while startTime < epochTime:
    temp_data = []
    temp_time = startTime
    while temp_time < startTime + 600:
        temp_data.append({
            "timestamp": temp_time,
            "temperature": getRandomFloat()
        })
        temp_time += 1
    data = {
        "start_timestamp": startTime,
        "end_timestamp": startTime + 600,
        "temperature": temp_data,
        "unit": "c",
        "serial_number": "0000000000000000000000000000000000000000000000000000000000000001"

    }
    startTime += 600
    print "1"
    full_data['data'].append(data)


    #viking.create(data)
r = requests.post("http://localhost:5000/api/viking", json=full_data)


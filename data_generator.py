import random
import time
import requests

from services.VikingService import VikingService


def getTimeEpoch():
    return time.time()


def getRandomFloat():
    return random.uniform(18.0, 22.0)


timeInSeconds = 60 * 60 * 24 * 30
epochTime = getTimeEpoch()
startTime = epochTime - timeInSeconds

viking = VikingService()

full_data = {
    "data": []
}

while startTime < epochTime:
    data = {
        "timestamp": startTime,
        "sensor_reading": float('%.3f'%(getRandomFloat())),
        "sensor_type": "temperature",
        "unit": "c",
        "serial_number": "3"

    }
    startTime += 600
    r = requests.post("http://localhost:5000/api/viking", json=data)

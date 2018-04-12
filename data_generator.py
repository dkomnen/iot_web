import random
import time
import requests

from services.VikingService import VikingService


def getTimeEpoch():
    return time.time()


def getRandomFloat():
    return random.randrange(20.0, 22.0)


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
        "temperature": getRandomFloat(),
        "unit": "c",
        "serial_number": "2"

    }
    startTime += 600
    r = requests.post("http://localhost:5000/api/viking", json=data)


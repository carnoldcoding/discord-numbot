import random
import requests
import os

WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK")

number = random.randint(0, 9)
# number2 = random.randint(0,9)

requests.post(WEBHOOK_URL, json={"content": str(number)})
# requests.post(WEBHOOK_URL, json={"content": str(number) + ", " + str(number2)})


# Comment for activity, again

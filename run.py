import time

import requests

import secrets

for route in secrets.ROUTES:
    requests.get(route)
    if secrets.DELAY:
        time.sleep(secrets.DELAY)
"""Basic connection example.
"""

import redis
from dotenv import load_dotenv
import os

load_dotenv()

r = redis.Redis(
    host=os.getenv("HOST"),
    port=os.getenv("PORT"),
    decode_responses=True,
    username=os.getenv("USERNAME"),
    password=os.getenv("PASSWORD"),
)

#success = r.set('foo', 'bar')
# True

#result = r.get('foo')

def getCache(country, city):
    return r.get(f"${country} ${city}")

def setCache(country, city, response):
    r.set(f"${country} ${city}", response)


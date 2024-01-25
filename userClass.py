from geopy.geocoders import Nominatim
from geopy.distance import distance

class userClass:
	def __init__(self, location, age, time, name):
                geolocator = Nominatim(user_agent='distance_calculator')
                self.location = geolocator.geocode(location, timeout = None)
                self.age = age
                self.time = time
                self.name = name

"""
location format 'street address, city, state zip, country'
will be stored as coordinates, accessed with .latitude and .longitude
Age can be an integer value
time will be two times, initially in 24hour format for conveniences sake
"""

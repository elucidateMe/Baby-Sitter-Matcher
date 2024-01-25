from geopy.geocoders import Nominatim
from geopy.distance import distance

class sitterClass:
    def __init__(self, location, preferredDistance, preferredAge, preferredTime, name):
        geolocator = Nominatim(user_agent='distance_calculator')
        self.location = geolocator.geocode(location, timeout = None)
        self.preferredDistance = preferredDistance
        self.preferredAge = preferredAge
        self.preferredTime = preferredTime
        self.name = name

"""
location format 'street address, city, state zip, country'
distance is just an integer radius
age is a 
time consists of open and close, e.g. 1500-0100
"""

from geopy.geocoders import Nominatim
from geopy.distance import distance

class rSitter:
	def __init__(self, location, pDistance, pAge, pTime, name):
                geolocator = Nominatim(user_agent='distance_calculator')
                self.location = geolocator.geocode(location, timeout = None)
                self.pDistance = pDistance
                self.pAge = pAge
                self.pTime = pTime
                self.name = name

"""
location format 'street address, city, state zip, country'
distance is just an integer radius
age is a 
time consists of open and close, e.g. 1500-0100
"""

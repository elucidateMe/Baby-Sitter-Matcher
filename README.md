# Baby Sitter Matcher
This is a general collection of classes which matches a suitable group of "sitters" for a "user"
GeoPy is utilized in order to calculate the distance between two addresses

## User Class
The "userClass" contains variables (location, age, and time) which are:
the location of the user (stored as latitude and longitude)
the age of child
time needed to be watched
```
def __init__(self, location, age, time, name):
    geolocator = Nominatim(user_agent='distance_calculator')
    self.location = geolocator.geocode(location, timeout = None)
    self.age = age
    self.time = time
    self.name = name
```

The name variable is currently utilized for bug testing and sanity checking.

## Sitter Class
The "sitterClass" contains variables (location, preferredDistance, preferredAge, and preferredTime) which are:
the location of the sitter (stored as latitude and longitude)
the preferredDistance the sitter is willing to travel
the preferred age range they will baby sit
the preferred times they will baby sit
```
def __init__(self, location, pDistance, pAge, pTime, name):
    geolocator = Nominatim(user_agent='distance_calculator')
    self.location = geolocator.geocode(location, timeout = None)
    self.pDistance = pDistance
    self.pAge = pAge
    self.pTime = pTime
    self.name = name
```

The name variable is currently utilized for bug testing and sanity checking.
## Matching Algorithm
The matching algorithm consists of multiple functions to determine whether the preferences of the sitter match the needs of the user.

### Distance Calculator
The user and sitter classes utilize GeoPy to calculate the latitude and longitude from an address.
"calculateDistance" uses the "distance" function within GeoPy to find the distance between two points in miles.
```
def calculateDistance(location1, location2):
    if location1 and location2:
        distanceInMiles = distance((location1.latitude, location1.longitude), 
                                  (location2.latitude, location2.longitude)).miles
        return distanceInMiles
    else:
        return None
```

### Time Checker
"timeCheck" returns true or false dependent on whether or not the users needed time is within the preferred time of the sitter
```
def timeCheck(tempUser, tempSitter):
    return ((tempUser.time[0] >= tempSitter.preferredTime[0]) and (tempUser.time[1] <= tempSitter.preferredTime[1]))
```

### Match Check
"matchChecker" compiles the distance calculator and time checker, as well as adds an age check, to return the sitter object and the distance of the .
```
def matchCheck(tempUser, tempSitter):
    location1 = tempUser.location
    location2 = tempSitter.location
    distanceInMiles = calculateDistance(location1, location2)
    if ((distanceInMiles <= tempSitter.preferredDistance) and (tempUser.age in tempSitter.preferredAge) and timeCheck(tempUser, tempSitter)):
        return (tempSitter, distanceInMiles)
```

### Match List
"matchList" takes a user and a list of sitters and outputs a list
```
def matchList(tempUser, listSitter):
    matchedSitterList = []
    for tempSitter in listSitter:
        matchedSitterList.append(matchCheck(tempUser, tempSitter))
    matchedSitterList = [i for i in matchedSitterList if i is not None]
    return matchedSitterList

```
There are some instances in which None is appended to the list as a result of the matchCheck function returning None, hence a list comprehension is used to remove such instances.
```
matchedSitterList = [i for i in matchedSitterList if i is not None]
```
This list comprehension does add an additional O(n) time complexity, which could be resolved by a placeholder variable that can be used in the above for loop to store the result of matchCheck, which may be worth it at the cost of a little space complexity and code "cleanness"
```
for tempSitter in listSitter:
    i = matchCheck(tempUser, tempSitter)
    if i != None:
        matchedSitterList.append(matchCheck(tempUser, tempSitter))
```

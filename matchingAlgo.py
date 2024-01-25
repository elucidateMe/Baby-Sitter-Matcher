from geopy.geocoders import Nominatim
from geopy.distance import distance
from geopy.exc import GeocoderTimedOut
from tempUserClass import userClass
from tempSitterClass import sitterClass

def calculateDistance(location1, location2):
    if location1 and location2:
        distanceInMiles = distance((location1.latitude, location1.longitude), 
                                  (location2.latitude, location2.longitude)).miles
        return distanceInMiles
    else:
        return None

def timeCheck(tempUser, tempSitter):
    return ((tempUser.time[0] >= tempSitter.preferredTime[0]) and (tempUser.time[1] <= tempSitter.preferredTime[1]))

def matchCheck(tempUser, tempSitter):
    location1 = tempUser.location
    location2 = tempSitter.location
    distanceInMiles = calculateDistance(location1, location2)
    if ((distanceInMiles <= tempSitter.preferredDistance) and (tempUser.age in tempSitter.preferredAge) and timeCheck(tempUser, tempSitter)):
        return (tempSitter, distanceInMiles)

def matchList(tempUser, listSitter):
    matchedSitterList = []
    for tempSitter in listSitter:
        matchedSitterList.append(matchCheck(tempUser, tempSitter))
    matchedSitterList = [i for i in matchedSitterList if i is not None]
    return matchedSitterList


if __name__ == "__main__":
    tempUser = userClass("23412 Amberwick Pl, Diamond Bar, CA 91765, USA", 7, (1145,2345), "Billy")
    tempSitter = sitterClass("1472 Spruce Tree Dr, Diamond Bar, CA 91765, USA", 20, list(range(6,12)), (0000,2359), "Mandy")

    #print(matchCheck(tempUser, tempSitter))

    listSitter = [
        tempSitter,
        sitterClass("1600 Grand Ave, Diamond Bar, CA 91765, USA", 200, [0], (0000,2359), "Grim"),
        sitterClass("1422 Summitridge Dr, Diamond Bar, CA 91765, USA", 0, [0], (0000,2359), "Erwin"),
        sitterClass("23506 Twin Spring Ln, Diamond Bar, CA 91765, USA", 200, list(range(0,17)), (0000,2359), "Sally"),
        sitterClass("1016 Park Spring Ln, Diamond Bar, CA 91765, USA", 200, list(range(0,17)), (0000,2359), "Gary")
        ]

    #print(listSitter)

    matchListList = matchList(tempUser, listSitter)
    print(matchListList)

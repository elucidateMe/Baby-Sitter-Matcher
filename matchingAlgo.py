from geopy.geocoders import Nominatim
from geopy.distance import distance
from geopy.exc import GeocoderTimedOut
from tempUserClass import rUser
from tempSitterClass import rSitter

def calculateDistance(location1, location2):
    if location1 and location2:
        distanceInMiles = distance((location1.latitude, location1.longitude), 
                                  (location2.latitude, location2.longitude)).miles
        return distanceInMiles
    else:
        return None

def timeCheck(tUser, tSitter):
    return ((tUser.time[0] >= tSitter.pTime[0]) and (tUser.time[1] <= tSitter.pTime[1]))

def matchCheck(tUser, tSitter):
    location1 = tUser.location
    location2 = tSitter.location
    distanceInMiles = calculateDistance(location1, location2)
    if ((distanceInMiles <= tSitter.pDistance) and (tUser.age in tSitter.pAge)) and timeCheck(tUser, tSitter):
        #print(tSitter.name)
        return (tSitter, distanceInMiles)
    else:
        pass

def matchList(tUser, lSitter):
    mSitter = []
    for tSitter in lSitter:
        mSitter.append(matchCheck(tUser, tSitter))
    mSitter = [i for i in mSitter if i is not None]
    return mSitter


if __name__ == "__main__":
    tUser = rUser("23412 Amberwick Pl, Diamond Bar, CA 91765, USA", 7, (1145,2345), "Billy")
    tSitter = rSitter("1472 Spruce Tree Dr, Diamond Bar, CA 91765, USA", 20, list(range(6,12)), (0000,2359), "Mandy")

    #print(matchCheck(tUser, tSitter))

    lSitter = [
        tSitter,
        rSitter("1600 Grand Ave, Diamond Bar, CA 91765, USA", 200, [0], (0000,2359), "Grim"),
        rSitter("1422 Summitridge Dr, Diamond Bar, CA 91765, USA", 0, [0], (0000,2359), "Erwin"),
        rSitter("23506 Twin Spring Ln, Diamond Bar, CA 91765, USA", 200, list(range(0,17)), (0000,2359), "Sally"),
        rSitter("1016 Park Spring Ln, Diamond Bar, CA 91765, USA", 200, list(range(0,17)), (0000,2359), "Gary")
        ]

    #print(lSitter)

    mList = matchList(tUser, lSitter)
    print(mList)

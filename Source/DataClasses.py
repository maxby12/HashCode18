
class Vehicle:

    def __init__(self, id):
        self.pos = [0, 0]
        self.id = id
        self.ride = None

class Ride:

    def __init__(self, id, startPos, endPos, startTime, endTime):
        self.id = id
        self.startPos = startPos
        self.endPos = endPos
        self.startTime = startTime
        self.endTime = endTime
        self.distance = distance(startPos, endPos)

    def isFactible(self, vehicle):
        return max(time + distance(vehicle.pos, self.startPos), self.startTime) + self.distance < self.endTime
    def getScore(self, vehicle):
        if (distance(vehicle.pos, self.startPos) + time <= self.startTime):
            return self.distance + bonus
        return self.distance
    def getFinishTime(self, vehicle):
        return max(time + distance(vehicle.pos, self.startPos), self.startTime) + self.distance


def distance(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

def getKey(item):
    return item[0]

def getMaxScoreRide(vehicle, rides):

    scores = []
    for ride in rides:
        if (ride.isFactible(vehicle)):
            scores.append( (ride.getScore(vehicle), ride.getFinishTime(vehicle), ride.id) )

    sorted(scores, key=getKey)
    return scores[:numVehicles]

def selectRide(rideOptions):

    maxScore = 0
    currentRide = 0
    vehicleToRide = 0

    for rideOption in rideOptions:
        if (rideOption[1][0] > maxScore):
            currentRide = rideOption[1][2]
            vehicleToRide = rideOption[0]
            maxScore = rideOption[1][0]


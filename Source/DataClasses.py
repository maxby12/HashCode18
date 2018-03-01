
class Vehicle:

    def __init__(self, id):
        self.pos = [0, 0]
        self.id = id
        self.ride = None
        self.isRiding = False
        self.listOfRides = []

    def updatePosition(self):
        if (self.isRiding):
            if (self.pos[0] != self.ride.endPos[0]):
                if (self.pos[0] > self.ride.endPos[0]): self.pos[0] -= 1
                else: self.pos[0] += 1
            elif (self.pos[1] != self.ride.endPos[1]):
                if (self.pos[1] > self.ride.endPos[1]): self.pos[1] -= 1
                else: self.pos[1] += 1
        else:
            if (self.pos[0] != self.ride.startPos[0]):
                if (self.pos[0] > self.ride.startPos[0]): self.pos[0] -= 1
                else: self.pos[0] += 1
            elif (self.pos[1] != self.ride.startPos[1]):
                if (self.pos[1] > self.ride.startPos[1]): self.pos[1] -= 1
                else: self.pos[1] += 1

        if (self.isRiding and self.pos[0] == self.ride.endPos[0] and self.pos[1] == self.ride.endPos[1]):
            self.ride = None
            self.isRiding = False
        if (not self.isRiding and self.pos[0] == self.ride.startPos[0] and self.pos[1] == self.ride.startPos[1]):
            self.isRiding = True


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
            scores.append( (ride.getScore(vehicle), ride.getFinishTime(vehicle), ride) )

    sorted(scores, key=getKey)
    return scores[:numVehicles]

def selectRide(rideOptions):

    while(len(rideOptions) > 0):

        maxScore = 0
        currentRideOption = None
        vehicleToRide = None

        for rideOption in rideOptions:
            if (rideOption[1][0][0] > maxScore or (rideOption[1][0][1]<currentRideOption[1][0][1] and rideOption[1][0][0] == maxScore)):
                currentRideOption = rideOption
                vehicleToRide = rideOption[0]
                maxScore = rideOption[1][0][0]

        vehicleToRide.ride = currentRideOption[1][0][2]
        vehicleToRide.listOfRides.append(vehicleToRide.ride.id)

        rideOptions.delete(currentRideOption)

        for rideOption in rideOptions:
            rideOptionList = [x for x in rideOption[1] if x[2].id != vehicleToRide.ride.id]


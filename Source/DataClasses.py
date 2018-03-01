
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

    def isFactible(self, vehicle, time):
        return max(time + distance(vehicle.pos, self.startPos), self.startTime) + self.distance < self.endTime


def distance(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

#from DataClasses import *

time = 0
time1 = 0
numVehicles = 0
rides = []
bonus = 0

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
        elif (not self.isRiding and self.pos[0] == self.ride.startPos[0] and self.pos[1] == self.ride.startPos[1]):
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

    while(len(rideOptions) > 0 and len(rideOptions[0][1]) > 0):

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

        rideOptions.remove(currentRideOption)

        global rides

        rides = [ride for ride in rides if ride.id != vehicleToRide.ride.id]

        for rideOption in rideOptions:
            rideOptionList = [x for x in rideOption[1] if x[2].id != vehicleToRide.ride.id]





def main(inpt):
    print("OPENING FILE "+inpt+"\n")
    rows = 0
    columns = 0
    number_rides =0
    vehicles = []
    
    def readData(inpt):
        file = open(inpt,'r')
        lines = file.readline()
        lines = lines.split(" ")
        rows = int(lines[0])
        columns = int(lines[1])
        global numVehicles
        numVehicles = int(lines[2])
        number_rides = int(lines[3])
        global bonus
        bonus = int(lines[4])
        global time1
        time1 = int(lines[5])
        for id in range(numVehicles):
            vehicles.append(Vehicle(id))
    
            
        lines = file.readlines()
        file.close()
        id = 0
        for line in lines:
            line = line.split(" ")
            init = [int(line[0]),int(line[1])]
            end = [int(line[2]),int(line[3])]
            earliest = int(line[4])
            latest = int(line[5])
            global rides
            rides.append(Ride(id,init,end,earliest,latest))
            id+=1
            
    readData(inpt)

    rideOptions = [[vehicle,getMaxScoreRide(vehicle,rides)] for vehicle in vehicles]
    selectRide(rideOptions)
    done = False
    for t in range(time1):
        if(not done):
            for vehicle in vehicles:
                vehicle.updatePosition()

        freeVehicles = [vehicle for vehicle in vehicles if vehicle.ride == None]
        rideOptions = [[vehicle,getMaxScoreRide(vehicle,rides)] for vehicle in freeVehicles]
        if(len(rideOptions[0][1]) <= 0):
            done = True
        selectRide(rideOptions)
        global time
        time+=1
                
    
    #OUTPUT
    file = open("file.out",'w')
    for v in vehicles:
        output = str(len(v.listOfRides))
        for i in v.listOfRides:
            output += " "+str(i)
        file.write(output+"\n")
    file.close()
        
        

def play():
    print("1-a-example.in\n2-b_should_be_easy.in\n3-c_no_hurry.in\n4-d_metropolis.in\n5-e_high_bonus.in")
    options = ["a_example.in","b_should_be_easy.in","c_no_hurry.in","d_metropolis.in","e_high_bonus.in"]
    #main(str(options[int(input())-1]))
    main("a_example.in")

play()





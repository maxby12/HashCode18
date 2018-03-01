frase = input("Hola!\n")
frase2 = input()
while(True):
    frase = input(frase+"\n")
    frase2 = input(frase2+"\n")




class Vehicle:
    currentPos = (0,0)
    ride = Ride((0,0),(0,0),0,0)
    
    
class Ride:
    startPos = (0,0)
    endPos = (0,0)
    startTime = 0
    endTime = 0
    
    def __init__(self, startPos, endPos, startTime, endTime):
            self.startPos = startPos
            self.endPos = endPos
            self.startTime = startTime
            self.endTime = endTime
    
    def getDistance(self):
        return abs(endPos[0] - startPos[0]) + abs(endPos[1] - startPos[1])      
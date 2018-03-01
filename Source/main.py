def main(inpt):
    print("OPENING FILE "+inpt+"\n")
    rows = 0
    columns = 0
    vehicles = 0
    rides =0
    bonus = 0
    steps = 0
    
    def readData(inpt):
        file = open(inpt,'r')
        lines = file.readline()
        lines = lines.split(" ")
        rows = int(lines[0])
        columns = int(lines[1])
        vehicles = int(lines[2])
        rides = int(lines[3])
        bonus = int(lines[4])
        steps = int(lines[5])
        print(rows,columns,vehicles,rides,bonus,steps)
    
            
        lines = file.readlines()
        for line in lines:
            line = line.split(" ")
            init = [int(line[0]),int(line[1])]
            end = [int(line[2]),int(line[3])]
            earliest = int(line[4])
            latest = int(line[5])
            print(init,end,earliest,latest)
            
    readData(inpt)
        

def play():
    print("1-a-example.in\n2-b_should_be_easy.in\n3-c_no_hurry.in\n4-d_metropolis.in\n5-e_high_bonus.in")
    options = ["a_example.in","b_should_be_easy.in","c_no_hurry.in","d_metropolis.in","e_high_bonus.in"]
    main(str(options[int(input())-1]))

play()





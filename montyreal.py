import random

WinnersKeep = 0
TotalEnd = 0
TotalWithBadEnding = 0


for i in range(1,10000+1):
    CarDoor = random.randint(1,3) #Door that hides the prize
    PlayerDoor = random.randint(1,3) #Door that the player chose as his door
    TotalWithBadEnding += 1
    #Select door to open
    SameDoor = True
    OpenedDoor = PlayerDoor
    while(SameDoor):
        OpenedDoor = random.randint(1,3)
        SameDoor = OpenedDoor == PlayerDoor or OpenedDoor == CarDoor
    if(OpenedDoor != CarDoor):
        #Let's assume the player always keeps his door at the end.
        #If his door number is the same as the winning door, he wins
        if(CarDoor == PlayerDoor):
            WinnersKeep +=1
        #Inc the amount of games that made it to the end no matter if he won or not
        TotalEnd += 1

print "Amount of situations where the game ended and the player won the car by keeping his door : "
print WinnersKeep
print "Total amount of games which made it to the end without revealing the car : "
print TotalEnd
print "Total amount of games : "
print TotalWithBadEnding
print "Percent of games that made it to the end that the player won by keeping his door : "
print float(WinnersKeep) / TotalEnd * 100

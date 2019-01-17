# I Bret McGee, student number 000207475, certify that all code submitted is my own work; that I have not copied it from any other source. I also certify that I have not allowed my work to be copied by others.

# Import random dumber inbetween 1-5 inclusive
import random
numberOfDisks = random.randint(  1, 5 )

# Set all variables
totalPrize = 0
numberOfPins = 0
currentPrize = 0
currentDisk = 0
slotValue = 0

while currentDisk < numberOfDisks:
    numberOfPins = 0
    currentDisk = currentDisk + 1
    print ( "Dropping Disk " + str( currentDisk ) )
    while numberOfPins < 5:
        currentPin = random.randint( 1, 100 )
        numberOfPins = numberOfPins + 1
        if currentPin <= 50:
            print( "tick" )
            slotValue = slotValue - 1
        else:
            print( "tock" )
            slotValue = slotValue + 1
    if slotValue == -5 or slotValue == -1 or slotValue == 1 or slotValue == 5:
        totalPrize = totalPrize + 0
        currentPrize = currentPrize + 0
        print( "The disk landed in the $" + str( currentPrize ) + " slot congratulations!" )
        currentPrize = 0
    elif slotValue == -4 or slotValue == 4:
        totalPrize = totalPrize + 100
        currentPrize = currentPrize + 100
        print( "The disk landed in the $" + str( currentPrize ) + " slot congratulations!" )
        currentPrize = 0
    elif slotValue == -3 or slotValue == 3:
        totalPrize = totalPrize + 500
        currentPrize = currentPrize + 500
        print( "The disk landed in the $" + str( currentPrize ) + " slot congratulations!" )
        currentPrize = 0
    elif slotValue == -2 or slotValue == 2:
        totalPrize = totalPrize + 1000
        currentPrize = currentPrize + 1000
        print( "The disk landed in the $" + str( currentPrize ) + " slot congratulations!" )
        currentPrize = 0
    else:
        totalPrize = totalPrize + 10000
        currentPrize = currentPrize + 10000
        print( "The disk landed in the $" + str( currentPrize ) + " slot congratulations!" )
        currentPrize = 0
prit( "Your total prize winning today is $" + str( totalPrize ) + "!" )

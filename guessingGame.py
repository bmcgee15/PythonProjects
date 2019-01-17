# I Bret McGee, student number 000207475, certify that all code submitted is my own work; that I have not copied it from any other source. I also certify that I have not allowed my work to be copied by others.

# Import random number inbetween 1 - 100
import random
randomNumber = random.randint( 1, 100 )

# Create guessStart & guessCounter
guessCounter = 0

# Create end game
gameOn = "true"

# Start game
while gameOn == "true":
    guessCounter = guessCounter + 1
# GET user input of a guess between 1 - 100
# ASSUME user will input valid characters    
    guess = int( input( "I Picked a number between 1 and 100 inclusive, can you guess it? " ) )

# Show Appropriate Messages

    if guess > randomNumber:
        print( "Sorry, my number is lower than that, try again! " )
    elif guess < randomNumber:
        print( "Sorry my number is higher, than that, try again! " )
    else:
        print( "Yes! That's correct! It took you " + str( guessCounter ) + " guesses to find my number." )
        gameOn = "false"
        
    

    
    
    

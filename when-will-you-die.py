# I Bret McGee, student number 000207475, certify that all code submitted is my own work; that I have not copied it from any other source. I also certify that I have not allowed my work to be copied by others.

# Pull Date
from datetime import datetime

# Get name
# ASSUME user will use propper characters
name = input( "What is your name? " )

# Display name
print( "Greetings earthling that goes by the name " + name )

# Ask for favourite hobby
favouriteHobby = input( "What is your favourite thing to to? " )

# Get birth year
# ASSUME user will use propper characters
birthYear = int( input( "What year were you born? " ) )

# Get current year
currentYear = datetime.now().year

# Calculate year of death
deathYear = str( currentYear - birthYear )

# Tell them when they will die
print( "You are : " + deathYear + " years old" )

# Ask them if they would like to know how
deathCause = input( " ... Would you like to know how you will die? " )
if deathCause == "no":
    print( "Well im going to tell you anyways... " + favouriteHobby )
elif deathCause == "nah":
    print( "Well im going to tell you anyways... " + favouriteHobby )
elif deathCause == "sure":
    print( "Unfortunately death by... " + favouriteHobby )
elif deathCause == "nope":
    print( "Well im going to tell you anyways... " + favouriteHobby )
elif deathCause == "yes":
    print( "Unfortunately death by... " + favouriteHobby )
elif deathCause == "yah":
    print( "Unfortunately death by... " + favouriteHobby )
elif deathCause == "yup":
    print( "Unfortunately death by... " + favouriteHobby )
else:
    print( "Not sure what that means, but unfortunately death by... " + favouriteHobby )

 

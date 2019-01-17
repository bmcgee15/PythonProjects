# I Bret McGee, student number 000207475, certify that all code submitted is my own work; that I have not copied it from any other source. I also certify that I have not allowed my work to be copied by others.

# Display ringing
print( "ring....ring....ring...." )

# Get input for Q1
# Assume user will input valid characters
sleeping = input( "Are you sleeping? " )

# IF sleeping is true print message
# IF sleeping is false GET user INPUT for Q2
if sleeping == "yes":
    print( "You will not answer the phone!" )
else:
    momCalling = input( "Is it your mom calling? " )
# If momCalling is true print message
# If momCalling is false Get user INPUT for Q3
    if momCalling == "yes":
        print( "You will answer the phone!" )
    else:
        morning = input( " Is it morning? " )
# If morning is true print "true" message
# If morning is false print "false" message
        if morning == "yes":
            print( "You will not answer it!" )
        else:
            print( "You will answer the phone!" )


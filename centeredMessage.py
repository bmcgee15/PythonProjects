# I Bret McGee, student number 000207475, certify that all code submitted is my own work; that I have not copied it from any other source. I also certify that I have not allowed my work to be copied by others.

# GET user input
strang = input( "Please enter a string less than 30 characters: " )

if len( strang ) > 30:
    print( "I'm sorry, your string is too long, goobye." )
else:
    print( "Your centered string is: " + strang.center(80) )

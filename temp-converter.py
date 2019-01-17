# I Bret McGee, student number 000207475, certify that all code submitted is my own work; that I have not copied it from any other source. I also certify that I have not allowed my work to be copied by others.

# GET temperature
# ASSUME user will use correct characters
temp = int( input( "What is the temperature? " ) )

# Get type of measure
getConvert = input( "is " + str( temp ) + " (C)elsius or (F)ahrenheit? : " )

# conversion types
fahCel = ( 5 / 9 ) * ( temp - 32 )
celFah = ( 9 / 5 ) * ( temp + 32 )

# Calculate conversion
if getConvert == "C":
    print( str( temp ) + "\xb0C is equal to " + str( celFah ) + "\xb0F! " )
elif getConvert == "F":
    print( str( temp ) + "\xb0F is equal to " + str( fahCel ) + "\xb0C! " )
elif getConvert == "c":
    print( str( temp ) + "\xb0C is equal to " + str( celFah ) + "\xb0F! " )
elif getConvert == "f":
    print( str( temp ) + "\xb0F is equal to " + str( fahCel ) + "\xb0C! " )
else:
    print( " HOW HARD IS IT TO ENTER A C OR F YOU FUCKING IDIOT?!?!!!?? " )

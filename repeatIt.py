# I Bret McGee, student number 000207475, certify that all code submitted is my own work; that I have not copied it from any other source. I also certify that I have not allowed my work to be copied by others.
keepGoing = False
number2 = 0
numbers = 0
while keepGoing == False:
    number1 = input( "Please pick a number between 1 and 15 ‘inclusive’ : " )
    if ( number1 == "1" or number1 == "2" or number1 == "3" or number1 == "4" or number1 == "5" or number1 == "6" or number1 == "7" or number1 == "8" or number1 == "9" or number1 == "10" or number1 == "11" or number1 == "12" or number1 == "13" or number1 == "14" or number1 == "15" ):
        keepGoing = True
    else:
        print( "I'm sorry, that number is not in range." )

number2 = input( "please pick a second number : " )
numbers = int( number1 ) * int( number2 )
repeatIt = ( numbers % 60 * "B" )
print( str( numbers ) + " modulo 60 is " + str( numbers % 60 ) + ":   " + repeatIt )


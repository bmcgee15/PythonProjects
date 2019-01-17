# I Bret McGee, student number 000207475, certify that all code submitted is my own work; that I have not copied it from any other source. I also certify that I have not allowed my work to be copied by others.

# GET input
# Assume user will input only number
number = int( input( "Pick a number between 1 and 20: " ) )

# Initialize sum to 0
numberSum = 0

# Initialize counter to 0
numberCounter = 0

# IF counter < number, increase counter by 1 and increase sum by number - counter
while numberCounter < number:
    numberCounter = numberCounter + 1
    numberSum = numberSum + ( number - numberCounter )

# If counter >= number show sum
else:
    print( numberSum )

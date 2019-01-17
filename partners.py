# I Bret McGee, student number 000207475, certify that all code submitted is my own work; that I have not copied it from any other source. I also certify that I have not allowed my work to be copied by others.

# GET user Row
# ASSUME user will only enter valid characters
userRow = input( "What row are you sitting in? " )

# GET user Column
# ASSUME user will only enter valid characters
userColumn = input( "What column are you sitting in? " )

# Get partner Row
# Assume user will only enter valid characters
partnerRow = input( "What row is your partner sitting in? " )

# Get partner Column
# Assume user will only enter valid characters
partnerColumn = input( "What column is your partner sitting in? " )

# Calculate Distance
distance = ((( int( userRow ) - int( partnerRow ) ) ** 2 ) + ( ( int( userColumn ) ) - int( partnerColumn ) ) **2 ) **0.5

# Print the results
print( "The instructor will approve this choice: " + str( distance > 3 ) )

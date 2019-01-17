def isTriple( a, b, c ):
	if a**2 + b**2 == c**2:
		tri = True
	elif a**2 + c**2 == b**2:
		tri = True
	elif c**2 + b**2 == a**2:
		tri = True
	else:
		tri = False
	return tri 

	
a = int( input( "Please enter a number: " ) )
	
b = int( input( "Please enter another number: " ) )

c = int( input( "Please enter yet another number: " ) )

tri = isTriple( a, b, c )

if tri == True:
	x = " form "
else:
	x = " do not form "

print( "The numbers " + str( a ) + ", " + str( b ) + ", " + str( c ) + x + "a Pythagorean tripple." )

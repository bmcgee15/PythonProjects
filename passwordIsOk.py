# I Bret McGee, student number 000207475, certify that all code submitted is my own work; that I have not copied it from any other source. I also certify that I have not allowed my work to be copied by others.

valid = False

def passOk( password ):
    if len( password ) <= 10:
        leastTen = False
        msg1 = "Your Password is LESS Than 10 Characters"
        print( msg1 )
    else:
        leastTen = True
    if any( i.isupper() for i in password ) == False:
        leastCap = False
        msg2 = "Your Password Does NOT Have a Capital Letter"
        print( msg2 )
    else:
        leastCap = True
    if any( i.isdecimal() for i in password ) == False:
        leastNum = False
        msg3 = "Your Password Does NOT Have a Number"
        print( msg3 )
    else:
        leastNum = True
    if ( "$" in password or "&" in password or "*" in password ) == False:
        leastSym = False
        msg4 = "Your Password Does NOT Have One of the Special Characters"
        print( msg4 )
    else:
        leastSym = True
    if ( " " in password ) == True:
        noSpace = False
        msg5 = "Your Password Has a Space"
        print( msg5 )
    else:
        noSpace = True
    if leastTen == False or leastCap == False or leastNum == False or leastSym == False or noSpace == False:
        global valid
        valid = False
    else:
        valid = True
    return valid


while valid == False:
    password = input(
        "Please enter a password that has at least 10 characters, 1 capital letter, 1 number, contains either $, & or * \n"
        "and does not have any spaces: ")
    passOk(password)
    if valid == False:
        print( "Please Try Again")
    else:
        break

print( "Password Accepted!" )
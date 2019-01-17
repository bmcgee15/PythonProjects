# implement the bubble sort algorithm by completing the module mysort
def mysort( myList ):
    return myList

def listCompare( list1, list2 ):
    sameList = len( list1 ) == len( list2 )

    if sameList == True:
        i = 0
        while i < len( list1 ):
            if list1[i] != list2[i] :
                sameList = False
                break
            i = i + 1
    return sameList

testData = [
    [7,3,9,4,10,2],
    [1,2,10,3,5,7,9,12],
    [1,2,3,4,5],
    [99, 98, 97, 96, 95, 94, 93, 92, 91]
    ]

for aList in testData:
    mySortedList = mysort( aList )
    sortedList = aList[:]
    sortedList.sort()

    if listCompare( mySortedList, sortedList):
        message = str( aList ) + " was correctly sorted to " + str( sortedList )
    else:
        message = str( aList ) + " was incorrectly sorted to " + str( sortedList )

    print( message )

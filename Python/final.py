"""
Function Name: puppyFinder()
Parameters: puppyCityDict (dict), cityDistanceDict (dict)
Returns: representation of puppy name, city and distance (str)
"""
def puppyFinder(cityDict, distanceDict):
    distanceList = []
    name = ""
    city = ""
    miles = 0
    for distance in distanceDict.values():
        distanceList.append(distance)
    distanceList.sort()
    miles = distanceList[0]
    for c in distanceDict:
        if distanceDict[c] == miles:
            city = c
    for n in cityDict:
        if cityDict[n] == city:
            name = n
    return "Your new puppy, {}, is in {} {} miles away.".format(name, city, str(miles)) 

            
#########################################
"""
Function Name: doubleOddhalfEven()
Parameters: numberList (list)
Returns: changedList (list)
"""
def doubleOddhalfEven(numberList):
    if len(numberList) == 0:
        return []
    else:
        if numberList[0] % 2 == 1:
            return sorted([numberList[0]*2] + doubleOddhalfEven(numberList[1:]))
        else:
            return sorted([int(numberList[0]/2)] + doubleOddhalfEven(numberList[1:]))

    
#########################################
"""
Function Name: datingApp()
Parameters: profile1 (list), profile2 (list)
Returns: compatibility (float)
"""
def datingApp(profile1, profile2):
    compatibility = 0
    sameInterest = []
    for interest in profile1[2]:
        if interest in profile2[2]:
            sameInterest.append(interest)
    totalInterest = []
    for interest in profile1[2]:
        if interest not in totalInterest:
            totalInterest.append(interest)
    for interest in profile2[2]:
        if interest not in totalInterest:
            totalInterest.append(interest)
    if abs(profile1[1] - profile2[1]) <= 5 and len(sameInterest) >= 3:
       compatibility = round((len(sameInterest)/len(totalInterest) * 100),1)
       return "You're {}% compatible!".format(str(compatibility))
    else:
        return "Sorry, you're incompatible."


#########################################
"""
Function Name: simplestDirections()
Parameters: directions(str)
Returns: simple direction (str)
"""
def simplestDirections(directions):
    udCounter = 0
    lrCounter = 0
    ud = ""
    lr = ""
    for m in directions:
        if m == "U":
            udCounter += 1
        if m == "D":
            udCounter -= 1 
        if m == ">":
            lrCounter += 1
        if m == "<":
            lrCounter -= 1
    if udCounter > 0:
        ud = "up"
    else:
        ud = "down"
    if lrCounter > 0:
        lr = "right"
    else:
        lr = "left"
    if udCounter == 0 and lrCounter == 0:
        return "No movement."
    else:
        return "You have moved {} blocks {} and {} blocks {}.".format(abs(udCounter), ud, abs(lrCounter), lr)


#########################################
"""
Function Name: songMystery()
Parameters: codedSong (str), songNames (list)
Returns: newSong (str)
"""
def songMystery(codedSong, songNames):
    codedList = []
    songList = []
    song = ""
    for char in codedSong.lower():
        codedList.append(char)
        codedList.sort()
    for s in songNames:
        for char in s.lower():
            songList.append(char)
            songList.sort()
        if songList == codedList:
            song = s.lower() 
            break
        else:
            songList = []
    if song == "":
        return "I need more clues :("
    else: 
        return song

#########################################
"""
Function Name: showToWatch()
Parameters: friendsFavShows (list) and favoriteShow (str)
Returns: list of friends (list)
"""


def showToWatch(friendsFavShows, favoriteShow):
    friendsList = []
    for i in range(len(friendsFavShows)):
        if favoriteShow in friendsFavShows[i][1]:
            friendsList.append(friendsFavShows[i][0])
    friendsList.sort()
    if len(friendsList) == 0:
        result = "Lonely night :("
    else:
        result = friendsList
    
    return result


#########################################
"""
Function Name: fixLabels()
Parameters: labelList (list)
Returns: list of correct labels (list)
"""
def fixLabels(labelList):
    namesList = []
    pricesList = []
    namepriceList = []
    correctList = []
    for label in labelList:
        if type(label) == str:
            namesList.append(label)
        if type(label) == float:
            pricesList.append(label)
    for i in range(len(namesList)):
        namepriceList.append([namesList[i], pricesList[i]])
    namepriceList.sort()
    for aList in namepriceList:
        aList = tuple(aList)
        correctList.append(aList)
    if len(namesList) == len(pricesList):
        result = correctList
    else:
        result = "Missing labels"
    return result


    
#########################################
"""
Function Name: newPlaylist()
Parameters: playlist (list)
Returns: list of songs (list)
"""
def newPlaylist(playlist):
    songsList = []
    namesList = []
    minutes = 0
    for i in range(len(playlist)):
        namesList.append(playlist[i][0])
    for i in range(len(playlist)):
        index = playlist[i][1].find(":")
        minutes += int(playlist[i][1][:index]) +int(playlist[i][1][index+1:])/60
    namesList.sort()
    roundedminutes = round(minutes, 2) 
    songsList.append(tuple(namesList))
    songsList.append(roundedminutes)
    return songsList


#########################################
"""
Function Name: birthdays()
Parameters: friends (list) and birthdates (list)
Returns: list of names (list)
"""
def birthdays(friends, birthdates):
    namesList =[]
    import calendar
    for i in range(len(birthdates)):
        if calendar.weekday(2022, birthdates[i][0], birthdates[i][1]) > 4:
            namesList.append(friends[i])
    namesList.sort()
    return namesList


#########################################
"""
Function Name: smashBros()
Parameters: fighterList (list), opponent (str)
Returns: list of good picks (list)
"""
def smashBros(fighterList, opponent):
    from smashData import counterPick
    emptyList = []
    for i in range(len(fighterList)):
        if fighterList[i] in counterPick(opponent):
            emptyList.append(fighterList[i])
    if len(emptyList) == 0:
        result = "No counters!"
    else:
        result = emptyList

    return result 
#########################################

"""
Function Name: findTicket()
Parameters: ticketDictionary (dict)
Returns: cheapestTicket (tuple)
"""
def findTicket(ticketDict):
    newList = sorted(ticketDict.values())
    if len(ticketDict) == 0: 
        cheapestTicket = "No tickets available!"
    else:
        for key, value in ticketDict.items():
            if value == newList[0]:
                cheapestTicket = (key, newList[0])     
    return cheapestTicket

    
#########################################

"""
Function Name: findHotel()
Parameters: hotelDictionary (dict)
Returns: preferredHotel (dict)
"""
def findHotel(hotelDict):
    aDict ={}
    maxscore = 0
    maxhotel =""
    finalDict ={}
    if len(hotelDict) ==0:
        preferredHotel = "No hotels available!"
    else:
        for key, value in hotelDict.items():
            if value not in aDict:
                aDict[value] = 1
            else:
                aDict[value] += 1
        for key, value in aDict.items():
            if value > maxscore:
                maxscore = value
                maxhotel = key
        finalDict[maxhotel] = maxscore
        preferredHotel = finalDict
    return preferredHotel

     
#########################################

"""
Function Name: findEvent()
Parameters: myInterests (list), schedule (dict)
Returns: match (list)
"""
def findEvent(myInterests, schedule):
    match = []
    for key,value in schedule.items():
        for interest in myInterests:
            if interest in value and key not in match:
                match.append(key) 
    return match


#########################################

"""
Function Name: figureSkating()
Parameters: technicalScores (list), componentScores (list)
Returns: finalScores (list)
"""
def figureSkating(technicalScores, componentScores):
    finalScores = []
    for i in range(len(technicalScores)):
        try:
            sum = technicalScores[i] + componentScores[i]
            finalScores.append(sum)
        except:
            continue
    return finalScores


#########################################

"""
Function Name: sportManagement()
Parameters: countryDict (dict)
Returns: sportDict (dict)
"""
def sportManagement(countryDict):
    sportDict = {}
    for key, value in countryDict.items():
        for sport in value:
            if sport not in sportDict:
                sportDict[sport] = [key]
            else:
                 sportDict[sport].append(key)
                 sportDict[sport].sort()
    return sportDict
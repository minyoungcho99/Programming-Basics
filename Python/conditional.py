
#########################################

"""
Function Name: workout()
Parameters: exerciseName (str), interestedFriends (int), totalFriends (int)
Returns: None (NoneType)
"""
def workout(exerciseName, interestedFriends, totalFriends):
    if interestedFriends/totalFriends < 0.2:
        print("Let's try a different workout.")
    elif 0.2 <= interestedFriends/totalFriends < 0.7:
        print("We will try to {} for 30 minutes.".format(exerciseName))
    else:
        print("We are so excited to {}!".format(exerciseName))

#########################################

"""
Function Name: iceCream()
Parameters: rating (float), distance (float)
Returns: choice (str)
"""
def iceCream(rating, distance):
    if rating == 4.5 and distance == 7.5:
        choice = "Jeni's"
        return choice 
    elif rating == 4.5 and distance == 3.6:
        choice = "Cold Stone"
        return choice
    elif rating == 4.5 and distance == 4.2:
        choice = "Morelli's"
        return choice
    elif rating == 4.0 and distance == 1.3:
        choice = "Bruster's"
        return choice
    elif rating == 4.0 and distance == 6.4:
        choice = "Sweet Stack"
        return choice
    elif rating == 3.5 and distance == 2.8:
        choice = "Baskin Robbins"
        return choice
    else:
        choice = "Try again tomorrow."
        return choice
    
#########################################

"""
Function Name: restaurantDecider()
Parameters: veganFriendly (bool), yelpStars (int), milesAway (int)
Returns: decisionStr (str)
"""
def restaurantDecider(veganFriendly, yelpStars, milesAway):
    if veganFriendly == False:
        decisionStr = "Not tonight."
        return decisionStr
    elif veganFriendly == True and yelpStars < 3:
        decisionStr = "Not good enough food."
        return decisionStr
    elif veganFriendly == True and yelpStars >= 3 and milesAway > 5:
        decisionStr = "Too far!"
        return decisionStr
    elif veganFriendly == True and yelpStars >= 3 and milesAway <= 5:
        decisionStr = "Perfect restaurant!"
        return decisionStr

#########################################

"""
Function Name: dinnerTip()
Parameters: numFriends (int), dinnerCost (float)
Returns: tipAmount (float)
"""
def dinnerTip(numFriends, dinnerCost):
    if numFriends <= 3:
        tipAmount = round(0.15 * dinnerCost, 2)
        return tipAmount
    elif 3 < numFriends <= 7:
        tipAmount = round(0.2 * dinnerCost, 2)
        return tipAmount
    else:
        tipAmount = round(0.25 * dinnerCost, 2)
        return tipAmount 

#########################################

"""
Function Name: planMaker()
Parameters: timeA (float), costA (int), timeB (float), costB (int)
Returns: planDecision (str)
"""
def planMaker(timeA, costA, timeB, costB):
    if costA > costB:
        planDecision = "planB"
        return planDecision
    elif costA < costB:
        planDecision = "planA"
        return planDecision
    elif costA == costB and timeA > timeB:
        planDecision = "planB"
        return planDecision   
    elif costA == costB and timeA < timeB:
        planDecision = "planA"
        return planDecision
    else:
        return "No plans this weekend."
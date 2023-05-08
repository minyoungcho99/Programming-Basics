#########################################

"""
Function Name: dinnerTime()
Parameters: N/A
Returns: None
"""
def dinnerTime():
    howManyEntrees = input("How many entrees will you be ordering?")
    howManyDrinks = input("How many drinks will you be ordering?")
    TotalCost = round(12 * int(howManyEntrees) + 4.5 * int(howManyDrinks), 2)
    print("The total cost of all the meals and drinks is ${}.".format(TotalCost))

#########################################

"""
Function Name: bottleBonanza().
Parameters: N/A
Returns: None
"""
def bottleBonanza():
    radius = input("What is the radius of the water bottle?")
    height = input("What is the height of the water bottle?")
    volume = round(3.14 * float(radius)**2 * float(height), 2)
    print("The volume of the water bottle is {}.".format(volume))

#########################################

"""
Function Name: winterBreak()
Parameters: N/A
Returns: None
"""
def winterBreak():
    episodes = input("How many episodes did you watch?")
    videos = input("How many YouTube videos did you watch?")
    totalTime = 40 * int(episodes) + 10 * int(videos)
    totalHours = totalTime // 60 
    totalMinutes = totalTime % 60 
    print("You spent {} hours and {} minutes watching Netflix and YouTube over winter break.".format(totalHours, totalMinutes))

#########################################

"""
Function Name: skateboardMoney()
Parameters: N/A
Returns: None
"""
def skateboardMoney():
    allowance = input("How much is your monthly allowance?")
    percentage = input("What percentage of your allowance do you want to save?")
    allowanceLeft = round(int(allowance) - int(allowance) * int(percentage)/100 - 30* (4.40 + 5.99), 2)
    print("You'll have ${} left to spend on your skateboard after savings and fees.".format(allowanceLeft))
#########################################

"""
Function Name: avgTotal()
Parameters: numString(str)
Returns: average(float)
"""


def avgTotal(numString):
    total = 0
    if numString == "":
        average = total / (len(numString) + 1) 
    else:
        for i in range(len(numString)):
            total += float(numString[i])
            average = total / len(numString)
    return average   

"""
Function Name: safeDecoder()
Parameters: characterString(str)
Returns: passcodeString(str)
"""


def safeDecoder(characterString):
    passcodeString = ""
    n= -1 
    for char in characterString:
        if char in "1234567890":
            n += 1
            passcodeString += str(n)
        else:
            n += 1               
    return passcodeString

"""
Function Name: testScore()
Parameters: test1(str), test2(str)
Returns: maxPercentage(float)
"""


def testScore(test1, test2):
    test1S = 0
    test2S = 0
    for num1 in test1:
        if num1 == "_":
            continue
        else:
            test1S += float(num1)
    for num2 in test2:
        if num2 == "_":
            continue
        else:
            test2S += float(num2)
    test1S *= 4
    test2S *= 4
    if test1S > test2S:
        maxPercentage = float(test1S)
    elif test1S < test2S:
        maxPercentage = float(test2S)
    else: 
        maxPercentage = "Same Percentage"
    return maxPercentage

"""
Function Name: trip()
Parameters: tripTotalCost(float), bankBalance(float), interestRate(float)
Returns: months(int)
"""


def trip(tripTotalCost, bankBalance, interestRate):
    totalBalance = bankBalance
    months = 0
    while totalBalance < tripTotalCost:
        totalBalance += (totalBalance*interestRate/100)
        months += 1 
    return months

"""
Function Name: rightTriangles()
Parameters: numRows(int), character(str)
Returns: None
"""

def rightTriangles(numRows, character):
    if numRows<2:
        print("No Triangle")
    else:
        for i in range(numRows+1):
            print(character*i)
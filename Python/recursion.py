#########################################
"""
Function Name: pageNumbers()
Parameters: bookList (list)
Returns: total (int)
"""
def pageNumbers(bookList):
    if len(bookList) == 0:
        return 0
    else:
        total = bookList[0] + pageNumbers(bookList[1:])
        return total

#########################################
"""
Function Name: letterPyramid()
Parameters: letter (str), rows (int)
Returns: None (NoneType)
"""
def letterPyramid(letter, rows):
    if letter.islower() == False:
        return 
    else:
        if rows == 0:
            return  
        else:
            letterPyramid(letter, rows-1)
            print(letter*(rows))
  
#########################################
"""
Function Name: specialChar()
Parameters: usernames (list)
Returns: aDict (dict)
"""
def specialChar(usernames):
    if len(usernames) == 0:
        return {}
    else:
        aDict = specialChar(usernames[1:])
        aDict[usernames[0]] = 0
        for char in usernames[0]:
            if char in ".-_!~#":
                aDict[usernames[0]] += 1
        return aDict 

#########################################
"""
Function Name: messageDecoder()
Parameters: hiddenMessage (str), characters (str)
Returns: decodedMessage (str)
"""

def messageDecoder(hidden, chars):
    if len(hidden) == 0:
        return ""
    if hidden[0] in chars:
        return messageDecoder(hidden[1:], chars) 
    else:
        return "" + hidden[0] + messageDecoder(hidden[1:], chars)

#########################################
"""
Function Name: stringCombiner()
Parameters: stringList (list)
Returns: combinedString (str)
"""
def stringCombiner(strList):
    combinedString = "" 
    if type(strList) == str:
        return strList
    else: 
        for string in strList:
            combinedString += stringCombiner(string)
    return combinedString
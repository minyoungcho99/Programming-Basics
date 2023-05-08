
#########################################

"""
Function Name: messageDecoder()
Parameters: message (str)
Returns: decodedMessage (str)
"""
def messageDecoder(message):
    decoded = ""
    for letter in message:
        if letter.isalpha():
            decoded += letter
        elif letter == " ":
            decoded += letter
        else:
            continue        
    if decoded == "":
        decodedMessage = "No message"  
    else: 
        decodedMessage = decoded[::-1]
    return decodedMessage


#########################################

"""
Function Name: clubMembers()
Parameters: interested (list), recruits (list)
Returns: memberList (list)
"""
def clubMembers(interested, recruits):
    memberList = []
    memberList += interested
    for item in recruits:
        if item in interested:
            continue
        else:
            memberList.append(item)
    return memberList
   
   
#########################################

"""
Function Name: checkCareer()
Parameters: students (list), career (str)
Returns: selectedStudents (list)
"""
def checkCareer(students, career):
    selectedStudents = []
    for i in range(len(students)):
        if students[i][1] == career:
            selectedStudents.append(students[i][0])
        else:
            continue
    selectedStudents.sort()
    return selectedStudents
   

#########################################

"""
Function Name: highGrades()
Parameters: students (list), gpas (list)
Returns: honorsStudents (list)
"""
def highGrades(students, gpas):
    honorsStudents = []
    for i in range(len(gpas)):
        if gpas[i] >= 3.5:
            honorsStudents.append(students[i])
        else:
            continue
    return honorsStudents

       
#########################################

"""
Function Name: quidditchPlay()
Parameters: playOrder (list), partners (list)
Returns: isApproved (bool)
"""


def quidditchPlay(playerOrder, partners):
    isApproved = False
    for i in range(len(playerOrder)):
        if partners[0] == playerOrder[i]:
            if playerOrder[abs(i-1)] == partners[1] or playerOrder[abs(i+1)] == partners[1]:
                isApproved = True

                print(isApproved, playerOrder[i])
            else:
                isApproved = False
                print(isApproved, playerOrder[i])
    return isApproved
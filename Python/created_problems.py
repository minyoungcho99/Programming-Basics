#### Problem 1

"""
Function Name: organizer()
Parameters: studentList (list)
Returns: majorDict (dict)
"""

#### Solution code:
def organizer(studentList):
    majorDict = {}
    if len(studentList) > 0: 
        for i in range(len(studentList)):
            if studentList[i][1] not in majorDict.keys():
                majorDict[studentList[i][1]] = [studentList[i][0]]
            else:
                majorDict[studentList[i][1]] += [studentList[i][0]]
        return majorDict
    else:
        return "No one has applied yet!"
            

#### Test case:
    # organizer([["Heidi", "Computer Science"], ["Sunny", "Computer Science"], 
    # ["Hunter", "Computer Engineering"], ["Lee", "Industrial Engineering"], 
    # ["Jay", "Electrical Engineering"], ["Chris", "Computer Science"], ["Vicky", "Biomedical Engineering"]])
    # should print:
    # {'Computer Science': ['Heidi', 'Sunny', 'Chris'], 
    # 'Computer Engineering': ['Hunter'], 'Industrial Engineering': ['Lee'], 
    # 'Electricial Engineering': ['Jay'], 'Biomedical Engineering': ['Vicky']}

 #### Problem 2

"""
Function Name: musicRecommender()
Parameters: fName (str), genre (str), year (int)
Returns: recommendedList (list)
"""

#### Solution code:
def musicRecommender(fName, genre, year):
    recommendedList = []
    csvFile = open(fName, 'r')
    data = csvFile.readlines()[1:]
    for line in data:
        line_pieces = line.strip().split(",")
        if line_pieces[2] == genre and int(line_pieces[3]) > year:
            recommendedList.append(line_pieces[1] + " - " + line_pieces[0])
    if len(recommendedList) == 0:
        return "Sorry, there is no corresponding song with your preferences :("

    else:
        recommendedList.sort()
        return recommendedList

#### Test case:
    # musicRecommender("musics.csv", "Pop", 2018)
    # should print:
    #['Ariana Grande - pov', 'Imagine Dragons - Enemy', 'Lizzo - Juice', 'Olivia Rodrigo - Deja vu']

 #### Problem 3

"""
Function Name: vowelCounter()
Parameters: lyric (str)
Returns: vowelNum (int) 
"""

#### Solution code:
def vowelCounter(lyric):
    if len(lyric) == 0:
        return 0
    else:
        if lyric[0].lower() in "aeiou":
            return 1 + vowelCounter(lyric[1:])
        else:
            return 0 + vowelCounter(lyric[1:])

#### Test case:
    # vowelCounter("They never even liked you in the first place")
    # should print: 
    # 14

#### Problem 4 

"""
Function Name: maxPrefCounter()
Parameters: pref (str)
Returns: maxpref (str)
"""
    
#### Solution code:
def maxPrefCounter(pref):
    aCounter = 0
    bCounter = 0
    cCounter = 0
    for char in pref:
        if char == "A":
            aCounter += 1
        elif char == "B":
            bCounter += 1
        else:
            cCounter += 1
    if aCounter > bCounter and aCounter > cCounter:
        return "A"
    elif bCounter > aCounter and bCounter > cCounter:
        return "B"
    elif cCounter > aCounter and cCounter > bCounter:
        return "C"
    else:
        return "Tie!"


#### Test case:
    # maxPrefCounter("ABABCCCBBACCABAC")
    # should print:
    # C

#### Problem 5

"""
Function Name: __init__ (method 1)
               __str__ (method 2)
               __lt__ (method 3)
Parameters: title (str), season(int), year (int), tomatometer (int), isOnNetflix (bool) (method 1)
            No parameter (method 2)
            other (method 3)
Returns: No return (method 1)
         indicator of the tomatometer of a show (str) (method 2)
         whether self's tomatometer is less than other's tomatometer (bool) (method 3)
"""
    
#### Solution code:

class Show:
    def __init__(self, title, season, year, tomatometer, isOnNetflix):
        self.title = title
        self.year = year
        self.tomatometer = tomatometer 
        self.season = season
        self.isOnNetflix = isOnNetflix
    def __str__(self):
        return "<{}> (Season {}, released {})'s tomatometer is {}%.".format(self.title, str(self.season), str(self.year), str(self.tomatometer))
    def __lt__(self, other):
        return self.tomatometer < other.tomatometer

#### Test case:
    strangerThings = Show("Stranger Things", 1, 2016, 97, True)
    bridgerton = Show("Bridgerton", 2, 2022, 79, True)

    # print(strangerThings)
    # should print:
    # <Stranger Things> (Season 1, released 2016)'s tomatometer is 97%.
    # print(strangerThings < bridgerton)
    # should print:
    # False

#########################################
"""
Function Name: featureActor()
Parameters: filename (str), actorName (str)
Returns: movieList (list)
"""
def featureActor(fName, aName):
    movieList = []
    aFile = open(fName, 'r')
    movieData = aFile.readlines()
    for i in range(1, len(movieData)):
        if movieData[i][:-1] == aName:  
            movieList.append(movieData[i-1][:-1])
            result = movieList
            break
        else:
            result = "Actor not found"
    aFile.close()
    return result

#########################################
"""
Function Name: alphabetSearch()
Parameters: filename (str), letter (str)
Returns: movieDict (dict)
"""
def alphabetSearch(fName, letter):
    aDict ={}
    aFile = open(fName, 'r')
    movieData = aFile.readlines()
    for i in range(1, len(movieData)):
        if letter == movieData[i][0].lower() and movieData[i-1] == "\n":
            aDict[movieData[i][:len(movieData[i])-1]] = movieData[i+1][:len(movieData[i+1])-1]
            result = aDict
    if len(aDict) == 0:
        result = "No movie tonight"
    aFile.close()
    return result

#########################################
"""
Function Name: favFilms()
Parameters: filename (str), movieList (list)
Returns: None (NoneType)
"""
def favFilms(fName, movieList):
    aList =[]
    aFile = open(fName, 'r')
    bFile = open("favMovies.txt", 'w')
    movieData = aFile.readlines()
    bFile.write(movieData[0] +"\n")
    for i in range(1, len(movieData)):
        for movie in movieList:
            if movieData[i][:-1] == movie:
                aList.append(movie)    
    for i in range(1, len(movieData)):
        for movie in movieList:
            if movieData[i][:-1] == movie and movie != aList[-1]:
                bFile.write(movieData[i])
                bFile.write(movieData[i+1])
                bFile.write(movieData[i+2])
                bFile.write("\n")
            if movieData[i][:-1] == movie and movie == aList[-1] and movieData[i+2][-1] == "\n":
                bFile.write(movieData[i])
                bFile.write(movieData[i+1])
                bFile.write(movieData[i+2][:-1])
            if movieData[i][:-1] == movie and movie == aList[-1] and movieData[i+2][-1] != "\n":
                bFile.write(movieData[i])
                bFile.write(movieData[i+1])
                bFile.write(movieData[i+2])
    bFile.close()
    aFile.close()

#########################################
"""
Function Name: movieNight()
Parameters: filename (str), timeLimit (int)
Returns: movie and average rating (tuple)
"""
def movieNight(fName, tLimit):
    aTup = ()
    maxAvg = 0
    csvFile = open(fName, 'r')
    data = csvFile.readlines()[1:]
    for line in data: 
        line_pieces=line.strip().split(",")
        time = int(line_pieces[3])
        imdb = int(line_pieces[1])
        rt = int(line_pieces[2])
        avg = round((imdb+rt)/2,2)
        if time <= tLimit:
            if avg > maxAvg: 
                maxAvg = avg
    for line in data:
        line_pieces=line.strip().split(",")
        time = int(line_pieces[3])
        imdb = int(line_pieces[1])
        rt = int(line_pieces[2])
        avg = round((imdb+rt)/2,2)
        if avg == maxAvg and time <= tLimit:
            mName = line_pieces[0]
            aTup = (mName, maxAvg)
            result = aTup
    if len(aTup) == 0:
        result = "Can't do movie night on Friday"
    return result

#########################################
"""
Function Name: movieRecs()
Parameters: filename (str), interestedList (list), expectedRatio (float)
Returns: recommendations (dict)
"""
def movieRecs(fName, intList, eRatio):
    aDict = {}
    csvFile = open(fName, 'r')
    data = csvFile.readlines()[1:]
    for line in data:
        line_pieces=line.strip().split(",")
        mName = line_pieces[0]
        time = int(line_pieces[3])
        imdb = int(line_pieces[1])
        rt = int(line_pieces[2])
        ratio = (imdb+rt)/2/time
        if mName in intList and ratio >= eRatio:
            aDict[mName] = time
    if len(aDict) == 0:
        result = "Too many expectations"  
    else:
        result = aDict
    return result

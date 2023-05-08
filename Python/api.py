
#########################################
"""
Function Name: highestPopulation()
Parameters: regionalBloc (str)
Returns: country with highest population (str)
"""
def highestPopulation(rBloc):
    maxPop = 0
    highCoun = ""
    import requests
    baseUrl = 'https://restcountries.com/v2/regionalbloc/'
    fullUrl = baseUrl + rBloc
    r = requests.get(fullUrl)
    data = r.json()
    for d in data:
        if d["population"] > maxPop:
            maxPop = d["population"]
            highCoun = d["name"]
    return highCoun 

#########################################
"""
Function Name: commonTimeZones()
Parameters: code1(str) , code2(str)
Returns: list of common time zones (list)
"""
def commonTimeZones(code1, code2):
    aList = []
    import requests
    baseUrl = 'https://restcountries.com/v2/alpha/'
    fullUrl1 = baseUrl + code1
    fullUrl2 = baseUrl + code2
    r1 = requests.get(fullUrl1)
    r2 = requests.get(fullUrl2)
    data1 = r1.json()
    data2 = r2.json()
    for t1 in data1["timezones"]:
        for t2 in data2["timezones"]:
            print(data1) 
            if t1 == t2:
                aList.append(t1)
    if len(aList) == 0:
        result = "No Common Time Zones"
    else:
        result = aList 
    return result    

#########################################
"""
Function Name: registerDomains()
Parameters: companyName (str), countryList (list)
Returns: list of domain names (list)
"""
def registerDomains(cName, cList):
    dList = []
    import requests
    baseUrl = 'https://restcountries.com/v2/name/'
    for country in cList:
        fullUrl = baseUrl + country
        r = requests.get(fullUrl)
        data = r.json()
        if data == {'status': 404, 'message': 'Not Found'}:
            continue
        else:
            dList.append(cName.lower() + data[0]["topLevelDomain"][0])
    return dList     

#########################################
"""
Function Name: findCountry()
Parameters: capitalList (list)
Returns: Dictionary mapping each capital to its country(dict)
"""
def findCountry(cList):
    cDict = {}
    import requests
    baseUrl = 'https://restcountries.com/v2/capital/'
    for capital in cList:
        fullUrl = baseUrl + capital
        r = requests.get(fullUrl)
        data = r.json()
        cDict[capital] = data[0]["name"]
    return cDict 

#########################################
"""
Function Name: commonLanguages()
Parameters: regionalBloc (str)
Returns: most common language (str) or languages (list)
"""
def commonLanguages(rBloc):
    lList = []
    counter = 0
    name = ""
    import requests
    baseUrl = 'https://restcountries.com/v2/regionalbloc/'
    fullUrl = baseUrl + rBloc
    r = requests.get(fullUrl)
    data = r.json()
    for cData in data:
        for dData in cData["languages"]:
            lList.append(dData["name"])
    newList = []
    for categories in lList:
        if counter < lList.count(categories):
            counter = lList.count(categories)
            name = categories
    newList.append(name) 
    for categories in lList:
        if counter == lList.count(categories):
            if categories not in newList:
                newList.append(categories)
    newList.sort()
    if len(newList) == 1:
        return name
    else:
        return newList
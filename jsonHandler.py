
def createResponseObj(responseList):
    respObj = []
    if responseList == 0:
        raise Exception("Error: Missing prediction data from model")
    for resp in responseList:
        respdict = {}
        respdict['fraud'] = resp
        respObj.append(respdict)
    if len(respObj) == 1:
        return respObj[0]
    return respObj

def parseJsonData(jsonData, colnames):
    data = []
    for element in jsonData:
        datapoint = []
        for col in colnames:
            datapoint.append(element[col])
        data.append(datapoint)
    return data
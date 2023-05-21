# 2023 HACKATHON

# for dataframes
import pandas as pd

# reading the data into a dictionary
data = pd.read_csv("pirate_attacks.csv")

# sorting the longitudes into a separate dictionary
longDict = data['longitude'].value_counts().to_dict()
maxLongAttacks = list(longDict.values())[0]
sortedLongKeys = sorted(longDict)
longDict = {i : longDict[i] for i in sortedLongKeys}

# sorting the latitudes into a separate dictionary
latDict = data['latitude'].value_counts().to_dict()
maxLatAttacks = list(latDict.values())[0]
sortedLatKeys = sorted(latDict)
latDict = {i : latDict[i] for i in sortedLatKeys}

# determining the final probability of a pirate attack
def prob(lat, long):
    return probLat(lat)*100, probLong(long)*100, (probLat(lat) * probLong(long))*100

# determining the probability of a pirate attack on a certain longitude
# takes in a longitude and returns a probability
def probLong(long):

    #
    if long in longDict.keys():
        prob = longDict[long]

    else:
        min = 0
        max = 0
        idx = 0
        for i in longDict.keys():
            if i < long:
                min = i
            elif i > long:
                max = i
                break
            idx += 1

        if abs(max-min) > 1.5 or abs(max-min) < 0.001:
            num = 1
        else:
            num = 5

        lowerBounds = sum([i for i in list(longDict.values())[idx-int(num*2):idx]])*round(num/2,1)
        upperBounds = sum([i for i in list(longDict.values())[idx:idx+int(num*2)]])*round(num/2,1)
        slope = (upperBounds - lowerBounds)/(max - min)
        y_intercept = lowerBounds - (slope * min)

        prob = slope * long + y_intercept

    return prob/maxLongAttacks

def probLat(lat):

    if lat in latDict.keys():
        prob = latDict[lat]

    else:
        min = 0
        max = 0
        idx = 0
        for i in latDict.keys():
            if i < lat:
                min = i
            elif i > lat:
                max = i
                break
            idx += 1

        if abs(max-min) > 1 or abs(max-min) < 0.001:
            num = 1
        else:
            num = 5

        lowerBounds = sum([i for i in list(latDict.values())[idx-int(num):idx]])*round(num/2,1)
        upperBounds = sum([i for i in list(latDict.values())[idx:idx+int(num)]])*round(num/2,1)
        slope = (upperBounds - lowerBounds)/(max - min)
        y_intercept = lowerBounds - (slope * min)

        prob = slope * lat + y_intercept

    return prob/maxLatAttacks

# TESTING
# print("prob near the strait of hormuz: " + str(round(prob(3.959, 5.664)[2], 3)) + "%")
# print("prob in the middle of the atlantic : " + str(round(prob(30.875, -40.711)[2], 3)) + "%")
# print("prob in malacca : " + str(round(prob(2.584, 100.93)[2], 3)) + "%")
# #print("prob on chattogram : " + str(round(prob(22.2166667, 91.7932)[2], 3)) + "%")
# print("prob near chattogram : " + str(round(prob(22.20838531160244, 91.79301474462983)[2], 3)) + "%")
# print("prob in mongolia : " + str(round(prob(47.404845545192046, 91)[2], 3)) + "%")
# print("prob in the caribbean sea : " + str(round(prob(10.227021951024312, -78.69188587875308)[2], 3)) + "%")
# print("prob near pakistan : " + str(round(prob(25.58394316888932, 66.53499889285015)[2], 3)) + "%")
# print("prob in the red sea : " + str(round(prob(29.785892, 48.867798)[2], 3)) + "%")


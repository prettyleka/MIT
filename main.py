import pandas as pd
from matplotlib import pyplot as plt

projectTwitterDataFile = open("project_twitter_data.csv", "r")
resultingDataFile = open("resulting_data.csv", "w")

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


def get_pos(strSentences):
    strSentences = strip_punctuation(strSentences)
    listStrSentences = strSentences.split()

    count = 0
    for word in listStrSentences:
        for positiveWord in positive_words:
            if word == positiveWord:
                count += 1
    return count


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())


def get_neg(strSentences):
    strSentences = strip_punctuation(strSentences)
    listStrSentences = strSentences.split()

    count = 0
    for word in listStrSentences:
        for negativeWord in negative_words:
            if word == negativeWord:
                count += 1
    return count


def strip_punctuation(strWord):
    for charPunct in punctuation_chars:
        strWord = strWord.replace(charPunct, "")
    return strWord


def writeInDataFile(resultingDataFile):
    resultingDataFile.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score")
    resultingDataFile.write("\n")

    linesPTDF = projectTwitterDataFile.readlines()
    #headerDontUsed = linesPTDF.pop(1)
    for linesTD in linesPTDF:
        listTD = linesTD.strip().split(',')
        resultingDataFile.write(
            "{}, {}, {}, {}, {}".format(listTD[1], listTD[2], get_pos(listTD[0]), get_neg(listTD[0]),
                                        (get_pos(listTD[0]) - get_neg(listTD[0]))))
        resultingDataFile.write("\n")


get_pos("licentious limited unwilling upbeat useful trust")
get_neg("licentious limited unwilling upbeat useful trust")
writeInDataFile(resultingDataFile)
projectTwitterDataFile.close()
resultingDataFile.close()

df=pd.read_csv("resulting_data.csv")
fig,ax=plt.subplots()
my_scatter_plot=ax.scatter(df[" Net Score"],df["Number of Retweets"])
plt.show()



nested1 = [1, 2, ['a', 'b', 'c'],['d', 'e'],['f', 'g', 'h']]
for x in nested1:
    print("level1: ")
    if type(x) is list:
        for y in x:
            print("     level2: {}".format(y))
    else:
        print(x)
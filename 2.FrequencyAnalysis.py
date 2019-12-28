import operator
import json


def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"


with open("PreparedData.json", "r", encoding="utf-8") as file:
    data = json.load(file)
    twitts = data[0]
    wordsFrequency = data[1]

numbTwitts = len(twitts)
wordsFrequency = {key: value for key, value in wordsFrequency.items()}
wordsFrequency = sorted(wordsFrequency.items(), key=operator.itemgetter(1))
wordsFrequency.reverse()
tmp = {}
for word in wordsFrequency:
    tmp[word[0]] = word[1]
wordsFrequency = tmp

with open('frequency.txt', 'w') as f:
    f.write("Word - number of occurrences of this word - percentage\n")
    for key in wordsFrequency:
        f.write(
            key + ' - ' + str(wordsFrequency[key]) + ' - ' + str(
                toFixed(wordsFrequency[key] / numbTwitts * 100, 2)) + '%\n')

twittsLen = {}
for twitt in twitts:
    if str(twitt['numbWords']) in twittsLen:
        twittsLen[str(twitt['numbWords'])] += 1
    else:
        twittsLen[str(twitt['numbWords'])] = 1

twittsLen = sorted(twittsLen.items(), key=operator.itemgetter(1))
twittsLen.reverse()
tmp = {}
for length in twittsLen:
    tmp[length[0]] = length[1]
twittsLen = tmp

with open('twits_length.txt', 'w') as f:
    f.write("Length - number of twitts - percentage\n")
    for key in twittsLen:
        f.write(key + ' - ' + str(twittsLen[key]) + ' - ' + str(
            toFixed(twittsLen[key] / numbTwitts * 100, 2)) + '%\n')

with open("PreparedData.json", "w", encoding="utf-8") as file:
    data = [twitts, wordsFrequency]
    json.dump(data, file)

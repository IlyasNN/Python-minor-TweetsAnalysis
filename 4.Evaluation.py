import json
import matplotlib.pyplot as plt


def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"


def emotionalAssessment1(wordsValues, twitts):
    negative = 0
    neutral = 0
    positive = 0
    for twitt in twitts:
        sumValue = 0
        for token in twitt['tokens']:
            if token in wordsValues:
                sumValue += wordsValues[token]
        twitt['assessment1'] = sumValue
        if sumValue >= 2:
            positive += 1
        elif 0 <= sumValue < 2:
            neutral += 1
        else:
            negative += 1

    with open('classifications.txt', 'w+') as file:
        file.write('Rule1 - sum of words\' values\n\n')

        file.write('\tPositive - ' + str(positive) + ' - ' + str(toFixed(positive / len(twitts) * 100, 2)) + '%\n')
        file.write('\tNeutral - ' + str(neutral) + ' - ' + str(toFixed(neutral / len(twitts) * 100, 2)) + '%\n')
        file.write('\tNegative - ' + str(negative) + ' - ' + str(toFixed(negative / len(twitts) * 100, 2)) + '%\n')

    x = ['positive', 'neutral', 'negative']
    y = [positive, neutral, negative]
    fig, ax = plt.subplots()

    ax.bar(x, y, color=['green', 'gold', 'red'], width=.5)
    for i, val in enumerate(y):
        plt.text(i, val, int(val), horizontalalignment='center', verticalalignment='bottom',
                 fontdict={'fontweight': 500, 'size': 12})

    plt.title("First rule - by sum of words' values")
    plt.ylabel('№ of twitts')
    ax.set_facecolor('seashell')
    fig.set_facecolor('floralwhite')

    plt.show()


def emotionalAssessment2(wordsValues, twitts):
    negative = 0
    neutral = 0
    positive = 0
    for twitt in twitts:
        curPositive = 0
        curNeutral = 0
        curNegative = 0

        for token in twitt['tokens']:
            if token in wordsValues:
                if wordsValues[token] == 1:
                    curPositive += 1
                elif wordsValues[token] == 0:
                    curNeutral += 1
                elif wordsValues[token] == -1:
                    curNegative += 1

        if curNeutral == max(curPositive, curNeutral, curNegative):
            twitt['assessment2'] = 0
            neutral += 1
        elif curPositive == max(curPositive, curNeutral, curNegative):
            twitt['assessment2'] = 1
            positive += 1
        elif curNegative == max(curPositive, curNeutral, curNegative):
            twitt['assessment2'] = -1
            negative += 1

    with open('classifications.txt', 'a+') as file:
        file.write('\nRule2 - sum of words\' values\n\n')

        file.write('\tPositive - ' + str(positive) + ' - ' + str(toFixed(positive / len(twitts) * 100, 2)) + '%\n')
        file.write('\tNeutral - ' + str(neutral) + ' - ' + str(toFixed(neutral / len(twitts) * 100, 2)) + '%\n')
        file.write('\tNegative - ' + str(negative) + ' - ' + str(toFixed(negative / len(twitts) * 100, 2)) + '%\n')

    x = ['positive', 'neutral', 'negative']
    y = [positive, neutral, negative]
    fig, ax = plt.subplots()

    ax.bar(x, y, color=['green', 'gold', 'red'], width=.5)
    for i, val in enumerate(y):
        plt.text(i, val, int(val), horizontalalignment='center', verticalalignment='bottom',
                 fontdict={'fontweight': 500, 'size': 12})

    plt.title("Second rule - by max number of type words")
    plt.ylabel('№ of twitts')
    ax.set_facecolor('seashell')
    fig.set_facecolor('floralwhite')

    plt.show()


def emotionalAssessment3(twitts):
    positiveNeutral = 0
    negative = 0
    badWords = []
    with open('Bad words.txt', 'r') as file:
        badWords = file.readlines()
        badWords = [word.rstrip() for word in badWords]

    for twitt in twitts:
        twitt['assessment3'] = 0
        for token in twitt['tokens']:
            if token in badWords:
                twitt['assessment3'] = -1

        if twitt['assessment3'] == -1:
            negative += 1
        else:
            positiveNeutral += 1

    with open('classifications.txt', 'a+') as file:
        file.write('\nRule3 - by the number of bad words\n\n')
        file.write('\tPositive and neutral- ' + str(positiveNeutral) + ' - ' + str(
            toFixed(positiveNeutral / len(twitts) * 100, 2)) + '%\n')
        file.write('\tNegative - ' + str(negative) + ' - ' + str(
            toFixed(negative / len(twitts) * 100, 2)) + '%\n')

        x = ['positive+neutral', 'negative']
        y = [positiveNeutral, negative]
        fig, ax = plt.subplots()

        ax.bar(x, y, color=['blue', 'red'], width=.5)
        for i, val in enumerate(y):
            plt.text(i, val, int(val), horizontalalignment='center', verticalalignment='bottom',
                     fontdict={'fontweight': 500, 'size': 12})

        plt.title("Third rule - by the number of bad words")
        plt.ylabel('№ of twitts')
        ax.set_facecolor('seashell')
        fig.set_facecolor('floralwhite')

        plt.show()


def emotionalAssessment4(wordsValues, twitts):
    negative = 0
    neutral = 0
    positive = 0
    for twitt in twitts:
        curPositive = 0
        curNeutral = 0
        curNegative = 0

        for token in twitt['tokens']:
            if token in wordsValues:
                if wordsValues[token] == 1:
                    curPositive += 1
                elif wordsValues[token] == 0:
                    curNeutral += 1
                elif wordsValues[token] == -1:
                    curNegative += 1

        if curPositive >= 2:
            twitt['assessment4'] = 1
            positive += 1
        elif curNegative >= 2:
            twitt['assessment4'] = -1
            negative += 1
        else:
            twitt['assessment4'] = 0
            neutral += 1

    with open('classifications.txt', 'a+') as file:
        file.write('\nRule4 - more then one word with this order: pos, neg , neu\n\n')

        file.write('\tPositive - ' + str(positive) + ' - ' + str(toFixed(positive / len(twitts) * 100, 2)) + '%\n')
        file.write('\tNeutral - ' + str(neutral) + ' - ' + str(toFixed(neutral / len(twitts) * 100, 2)) + '%\n')
        file.write('\tNegative - ' + str(negative) + ' - ' + str(toFixed(negative / len(twitts) * 100, 2)) + '%\n')

    x = ['positive', 'neutral', 'negative']
    y = [positive, neutral, negative]
    fig, ax = plt.subplots()

    ax.bar(x, y, color=['green', 'gold', 'red'], width=.5)
    for i, val in enumerate(y):
        plt.text(i, val, int(val), horizontalalignment='center', verticalalignment='bottom',
                 fontdict={'fontweight': 500, 'size': 12})

    plt.title("Forth rule - more then one word with this order: pos, neg , neu")
    plt.ylabel('№ of twitts')
    ax.set_facecolor('seashell')
    fig.set_facecolor('floralwhite')

    plt.show()


with open("PreparedData.json", "r", encoding="utf-8") as file:
    data = json.load(file)
    twitts = data[0]
    wordsFrequency = data[1]

wordsValues = {}
with open('estimations.txt', 'r') as f:
    for line in f.readlines():
        word = line.split()
        wordsValues[word[0]] = int(word[1])

emotionalAssessment1(wordsValues, twitts)
emotionalAssessment2(wordsValues, twitts)
emotionalAssessment3(twitts)
emotionalAssessment4(wordsValues, twitts)

with open("PreparedData.json", "w", encoding="utf-8") as file:
    data = [twitts, wordsFrequency]
    json.dump(data, file)

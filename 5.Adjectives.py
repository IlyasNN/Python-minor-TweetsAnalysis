import json
import pymorphy2
import matplotlib.pyplot as plt


def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"


morph = pymorphy2.MorphAnalyzer()

with open("PreparedData.json", "r", encoding="utf-8") as file:
    data = json.load(file)
    twitts = data[0]
    wordsFrequency = data[1]

wordsValues = {}
with open('estimations.txt', 'r') as f:
    for line in f.readlines():
        word = line.split()
        wordsValues[word[0]] = int(word[1])

numPosAdj = 0
numNegAdj = 0
posAdjList = []
negAdjList = []

itr = iter(wordsFrequency)

while numPosAdj != 5 or numNegAdj != 5:
    word = next(itr)
    wordParsed = morph.parse(word)[0]
    if wordParsed.tag.POS == 'ADJF' and wordsValues[word] == 1 and numPosAdj < 5:
        posAdjList.append(word)
        numPosAdj += 1
    elif wordParsed.tag.POS == 'ADJF' and wordsValues[word] == -1 and numNegAdj < 5:
        negAdjList.append(word)
        numNegAdj += 1

numbTwitts = len(twitts)
with open('adjectives.txt', 'w') as f:
    f.write('Top-5 Positive:\n')
    for word in posAdjList:
        f.write(word + ' - ' + str(wordsFrequency[word]) + ' - ' + str(
            toFixed(wordsFrequency[word] / numbTwitts * 100, 2)) + '%\n')

    f.write('\nTop-5 Negative:\n')
    for word in negAdjList:
        f.write(word + ' - ' + str(wordsFrequency[word]) + ' - ' + str(
            toFixed(wordsFrequency[word] / numbTwitts * 100, 2)) + '%\n')

x1 = posAdjList
y1 = [wordsFrequency[word] for word in posAdjList]
x2 = negAdjList
y2 = [wordsFrequency[word] for word in negAdjList]
fig, (ax1, ax2) = plt.subplots(2, 1)

plt.title('Top 5 posotive and negative adjectives')

ax1.bar(x1, y1, color=['green'], width=.5)
ax2.bar(x2, y2, color=['red'], width=.5)
for i, val in enumerate(y1):
    ax1.text(i, val, int(val), horizontalalignment='center', verticalalignment='bottom',
             fontdict={'fontweight': 500, 'size': 8})

for i, val in enumerate(y2):
    ax2.text(i, val, int(val), horizontalalignment='center', verticalalignment='bottom',
             fontdict={'fontweight': 500, 'size': 8})

ax1.title.set_text('Top 5 positive adjectives')
ax1.set_ylabel('The number of occurrences of the word in tweets')
ax1.set_facecolor('seashell')

ax2.title.set_text('Top 5 negative adjectives')
ax2.set_ylabel('The number of occurrences of the word in tweets')
ax2.set_facecolor('seashell')

fig.set_facecolor('lightgrey')

plt.show()

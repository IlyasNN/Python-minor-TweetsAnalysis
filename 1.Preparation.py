import pymorphy2
import time
import string
import json

morph = pymorphy2.MorphAnalyzer()

with open('data.txt', encoding='utf-8-sig') as f:
    lines = f.readlines()

wordsFrequency = {}
twitts = []
for line in lines:
    if line == '\n':
        pass
    else:
        curTwitt = {}
        curTwitt['original'] = line
        twittDate = line[0:16]
        twittDate = time.strptime(twittDate, '%Y-%m-%d %H:%M')
        curTwitt['date'] = twittDate

        for ch in string.punctuation:
            line = line.replace(ch, '')
        tokens = line.split()

        forAnalyse = {'NOUN', 'ADJF', 'INFN', 'ADVB', 'VERB', 'PRTF', 'PRTS', 'GRND'}
        # forAnalyse = {'NOUN', 'ADJF', 'INFN', 'ADVB'}
        # forAnalyse = {'VERB', 'PRTF', 'PRTS', 'GRND'}

        tokens = [morph.parse(token)[0] for token in tokens]
        tokens = [token for token in tokens if token.tag.POS is not None]
        curTwitt['numbWords'] = len(tokens)
        tokens = [token.normal_form for token in tokens if token.tag.POS in forAnalyse]
        curTwitt['tokens'] = tokens
        for token in tokens:
            if token in wordsFrequency:
                wordsFrequency[token] += 1
            else:
                wordsFrequency[token] = 1
        twitts.append(curTwitt)

with open("PreparedData.json", "w", encoding="utf-8") as file:
    data = [twitts, wordsFrequency]
    json.dump(data, file)

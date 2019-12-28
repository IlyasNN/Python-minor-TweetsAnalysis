import json
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"


with open("PreparedData.json", "r", encoding="utf-8") as file:
    data = json.load(file)
    twitts = data[0]
    wordsFrequency = data[1]

twitts.reverse()
startTime = datetime(2018, 7, 7, 23, 50, 00)

endTime = datetime(2018, 7, 11, 1, 30, 00)

graph = []

delta = 30
x = []
ypos = []
yneu = []
yneg = []
ysum = []
format = '%m.%d %H:%M'

curTime = startTime + timedelta(minutes=delta)
with open('hours.txt', 'w') as file:
    while curTime < endTime:
        sum = 0
        pos = 0
        neu = 0
        neg = 0
        itr = iter(twitts)
        twitt = next(itr)
        while datetime(*twitt['date'][0:7]) < curTime:
            sum += 1
            if twitt['assessment1'] >= 2:
                pos += 1
            elif twitt['assessment1'] < 0:
                neg += 1
            else:
                neu += 1

            twitt = next(itr)

        file.write(
            startTime.strftime(format) + ' - ' + curTime.strftime(format) + ' : ' + str(sum) + ' ' + str(toFixed((
                    pos / sum), 2)) + '/' + str(toFixed((neu / sum), 2)) + '/' + str(toFixed((neg / sum), 2)) + '\n')

        x.append(curTime)
        ypos.append(pos / sum)
        yneu.append(neu / sum)
        yneg.append(neg / sum)
        ysum.append(sum)

        curTime = curTime + timedelta(minutes=delta)

    sum = 0
    pos = 0
    neu = 0
    neg = 0
    itr = iter(twitts)
    twitt = next(itr)
    while datetime(*twitt['date'][0:7]) < endTime:
        sum += 1
        if twitt['assessment1'] >= 2:
            pos += 1
        elif twitt['assessment1'] < 0:
            neg += 1
        else:
            neu += 1
        try:
            twitt = next(itr)
        except StopIteration:
            break

    file.write(startTime.strftime(format) + ' - ' + endTime.strftime(format) + ' : ' + str(sum) + ' ' + str(toFixed((
            pos / sum), 2)) + '/' + str(toFixed((neu / sum), 2)) + '/' + str(toFixed((neg / sum), 2)) + '\n')

    x.append(endTime)
    ypos.append(pos / sum)
    yneu.append(neu / sum)
    yneg.append(neg / sum)
    ysum.append(sum)

x = x[::5]
ysum = ysum[::5]
ypos = ypos[::5]
yneu = yneu[::5]
yneg = yneg[::5]

ax1 = plt.subplot(2, 1, 1)
ax1.set_title('Распределение кол-ва твитов и их типо по времени')
ax1.set_xticks(x)
ax1.grid()
ax1.set_xticklabels(['' for i in range(0, len(x))])
ax1.plot(x, ypos, 'g-', label='pos')
ax1.scatter(x, ypos, color='g', s=15)
ax1.plot(x, yneu, 'y-', label='neu')
ax1.scatter(x, yneu, color='y', s=15)
ax1.plot(x, yneg, 'r-', label='neg')
ax1.scatter(x, yneg, color='r', s=15)
plt.ylabel('Расппределение', fontsize=15)

ax1.legend()

ax2 = plt.subplot(2, 1, 2)
ax2.vlines(x, 0, ysum, color='blue')
ax2.scatter(x, ysum, color='blue', s=20)
ax2.set_xticks(x)
ax2.grid()
ax2.set_xticklabels([x[i].strftime(format) for i in range(0, len(x))], fontsize=7, rotation=50, ha='right')
plt.ylabel('Кол-во твитов', fontsize=15)
plt.xlabel('Временные отрезки', fontsize=15)



plt.show()

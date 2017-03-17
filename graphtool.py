import csv
import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as ticker
datePoints = []
profitPoints = []
cumulativeProfit = []
totalProfit = 0.0

for line in open("Trade_History.csv"):
    try:
        strippedLine = line.split(',')
        datePoints.append(dt.datetime.strptime(strippedLine[0].split()[0],'%m/%d/%Y').date())
        profit = strippedLine[5]
        if(profit[0] == "("):
            profitPoints.append(float(profit[2:-1])*(-1))
        else:
            profitPoints.append(float(profit[1:]))
    except:
        pass

datePoints.reverse()
profitPoints.reverse()
for item in profitPoints:
    totalProfit += item
    cumulativeProfit.append(totalProfit)
fig = plt.figure()           
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%Y'))
plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
plt.plot(datePoints,cumulativeProfit)
plt.gcf().autofmt_xdate()
plt.show()
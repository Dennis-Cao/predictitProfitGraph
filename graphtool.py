import csv
import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as ticker
import sys

if(len(sys.argv) != 2):
    print("Incorrect argument. Please use the following format:")
    print("python graphtool.py (Insert Trade History File Here, no parenthesis)")
    sys.exit(1)
try:
    csvFile = open(sys.argv[1])
except:
    print(sys.argv[1] + " not found. Please ensure the file exists.")
    sys.exit(1)
datePoints = []
profitPoints = []
fees = []
totalProfit = 0.0
totalFees = 0.0
for line in csvFile:
    try:
        strippedLine = line.split(',')
        datePoints.append(dt.datetime.strptime(strippedLine[0].split()[0],'%m/%d/%Y').date())
        profit = strippedLine[5]
        fees.append(float(strippedLine[6][2:-1])*(-1))
        if(profit[0] == "("):
            profitPoints.append(float(profit[2:-1])*(-1))
        else:
            profitPoints.append(float(profit[1:]))
    except:
        pass

csvFile.close()
datePoints.reverse()
profitPoints.reverse()
cumulativeProfit = []
cumulativeProfitMinusFees = []

for i in range(len(profitPoints)):
    totalProfit += profitPoints[i]
    totalFees -= fees[i]
    cumulativeProfit.append(totalProfit)
    cumulativeProfitMinusFees.append(totalProfit-totalFees)

fig = plt.figure()   
fig.set_size_inches(18.5, 10.5, forward=True)        
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%Y'))
plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
plt.plot(datePoints,cumulativeProfit)
plt.plot(datePoints,cumulativeProfitMinusFees)
plt.gcf().autofmt_xdate()
plt.legend(['Profit before fees', 'Profit after fees'], loc='upper left')
plt.show()
import matplotlib.pyplot as plt
import numpy as np
fbiFile = open("FBI.txt")
concertFile = open("concerts.txt")

fbiList = fbiFile.readlines()
concertList = concertFile.readlines()

print(fbiList)
print(concertList)
for i in range(len(fbiList)):
    fbiList[i] = float(fbiList[i])
for j in range(len(concertList)):
    concertList[j] = float(concertList[j])
x = [2000, 2002.5, 2005, 2007.5, 2010, 2012.5, 2015, 2017.5, 2020]
x1 = [2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019]
y = (0, 250000, 500000, 750000, 1000000, 1250000, 1500000, 1750000, 2000000)
z = [0, 25, 50, 75, 100, 125, 150, 175, 200]
print(fbiList)
print(concertList)
with plt.xkcd():
    #t = np.arange(0.01, 10.0, 0.01)
    data1 = fbiList
    data2 = concertList
    #fig = plt.subplot()
    fig, ax1 = plt.subplots()
    ax1 = plt.subplot()
    color = "tab:red"
    ax1.set_xlabel("Years")
    ax1.set_ylabel('Crimes', color = color)
    ax1.plot(x1, data1, color=color)
    ax1.tick_params(axis='y', labelcolor = color)
    #ax1.set_yticks(np.arange(min(y), max(y)+1,2.0))
    ax2 = ax1.twinx()
    #ax2 = plt.subplot()
    color = "tab:blue"
    ax2.set_ylabel('Plaintain Consumption Per Capita (kG)', color=color)
    ax2.plot(x1, data2, color=color)
    ax2.tick_params(axis='y', labelcolor = color)
    fig.tight_layout()
    plt.show()
    '''
    plt.plot(range(2000,2020),fbiList,color="blue", marker='x',markersize=10)
    plt.plot(range(2000,2020), concertList, color="red", marker="x", markersize=10)
    plt.axis([2000,2020,0,2000000])
    plt.xlabel("Years")
    plt.ylabel("Violent Crimes")
    plt.xticks(np.arange(min(x), max(x)+1,2.0))
    plt.yticks(np.arange(min(y), max(y)+1,250000))
    '''

plt.show()
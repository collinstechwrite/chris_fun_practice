import json 
import urllib
import re
import requests
import matplotlib.pyplot as plt
import datetime



"""
plt.barh(*zip(*ExchangeRatesDict.items()))
plt.show()
"""



"""
Get historical rates for any day since 1999.
https://api.exchangeratesapi.io/2010-01-12
"""



todaysdate = datetime.date.today()
print('Current date: ', todaysdate)




print("CHECKING FOREIGN EXCHANGE RATES AND DATES")
linkforpopular = ("https://api.exchangeratesapi.io/" + str(todaysdate)) 
zz = requests.get(linkforpopular)
populardata = zz.text


indexrates = populardata.index(':')
indexbase = populardata.index(',"base"')


ExchangeRatesDict = json.loads(populardata[indexrates+1:indexbase]) #convert pulled data to dictionary



"""https://api.exchangeratesapi.io/2010-01-12"""
"""Get historical rates for any day since 1999."""

mydate = input("enter any date from 1999 in this format 2010-01-12")


linkforpopular = ("https://api.exchangeratesapi.io/" + str(mydate)) 
zz = requests.get(linkforpopular)
populardata = zz.text


indexrates = populardata.index(':')
indexbase = populardata.index(',"base"')


ExchangeRatesDict2 = json.loads(populardata[indexrates+1:indexbase]) #convert pulled data to dictionary



intersect = [] #only where foreign exchange symbols from dictionary 1 can be found in dictionary2
for item in ExchangeRatesDict.keys(  ):
    if item in ExchangeRatesDict2:
        intersect.append(item)


print('{:10} {:10} {:10} {:20}'.format('Currency', str(todaysdate) , str(mydate), 'Difference',))


for item in intersect:
    print ('{:10} {:10} {:10} {:20}'.format(item,ExchangeRatesDict[item],ExchangeRatesDict2[item],ExchangeRatesDict[item] - ExchangeRatesDict2[item]))




    



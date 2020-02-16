#imports needed for extracting
import sys
import urllib
import re
import requests

#used for sorting python dictionary
import operator

#imports needed for plotting graph
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt


myinput = input("Input a keyword of an item that you want to buy:")
priceinputmin = input("Input a minimum price:")
priceinputmax = input("Input a maximum price:")
zipcode = input("Input zipcode near seller:")
zipcode2 = input("Input COMPARISON zipcode near seller:")
distancetozipcode = input("Distance radius from seller zipcode:")
limit = int(input("input result limit 1-100:"))




def AnalyseAnItemIDForTitle(analyse):
    
    try:
        linkforfindinghowmanysold = ("https://www.ebay.com/itm/" + analyse)
        h = requests.get(linkforfindinghowmanysold)
        mostsolddata = h.text
        extractMostSoldonEbay = re.findall('<title>(.+?)  | eBay</title>', mostsolddata)
        apple = str(extractMostSoldonEbay)
        az = apple[2:-2]

        if az == "":
            linkforfindinghowmanysold = ("https://www.ebay.com/itm/" + analyse)
            h = requests.get(linkforfindinghowmanysold)
            mostsolddata = h.text
            extractMostSoldonEbay = re.findall('<meta name="description" content="(.+?)" />', mostsolddata)
            apple = str(extractMostSoldonEbay)
            az = apple[2:-2]
            return az
        

        return az
    except Exception:
        abz = 0
        return abz

def pricefix(qb):
    
    try:
        pricef = float(qb)
        return pricef

    except Exception:

        qb = 0
        return qb


def AnalyseAnItemID(analyse):


    try:
        linkforfindinghowmanysold = ("https://www.ebay.com/itm/" + analyse)
        h = requests.get(linkforfindinghowmanysold)
        mostsolddata = h.text
        extractMostSoldonEbay = re.findall('">(.+?) sold</a></span>', mostsolddata)
        apple = str(extractMostSoldonEbay)
        apple = apple.replace(',', '')
        ap = apple[2:-2]
        az = int(ap)

        return az
    except Exception:
        abz = 0
        return abz


def AnalyseAnItemIDForhours(analyse2):
    try:
        linkforfindinghowmanysold = ("https://www.ebay.com/itm/" + analyse2)
        h = requests.get(linkforfindinghowmanysold)
        mostsolddata = h.text
        extractMostSoldonEbay = re.findall('>(.+?) sold in last 24 hours</span>', mostsolddata)
        apple = str(extractMostSoldonEbay)
        apple = apple.replace(',', '')
        ap = apple[2:-2]
        az = int(ap)
  
        return az
    except Exception:
        abz = 0
        return abz



def AnalyseItemIDForPrice(analyse):


    try:
        linkforfindinghowmanysold = ("https://www.ebay.com/itm/" + analyse)
        h = requests.get(linkforfindinghowmanysold)
        mostsolddata = h.text
        extractMostSoldonEbay = re.findall('">US(.+?)</span>', mostsolddata)
        apple = str(extractMostSoldonEbay)
        apple = apple.replace('$', '')
        apple = apple.replace(' ', '')
        apple = apple.replace('/ea','')
        ap = apple[2:-2]
        az = ap
       
        return az
    except Exception:
        abz = 0
        return abz




def AnalyseAnItemIDForWatchers(analyse2):
    try:
        linkforfindinghowmanysold = ("https://www.ebay.com/itm/" + analyse2)
        h = requests.get(linkforfindinghowmanysold)
        mostsolddata = h.text
        extractMostSoldonEbay = re.findall('defaultWatchCount":(.+?),', mostsolddata)
        apple = str(extractMostSoldonEbay)
        apple = apple.replace(',', '')
        ap = apple[2:-2]
        az = int(ap)
   
        return az
    except Exception:
        abz = 0
        return abz


def BMP(s):
    return "".join((i if ord(i) < 10000 else '\ufffd' for i in s))



def unescape(s):
    s = s.replace("&lt;", "<")
    s = s.replace("&gt;", ">")
    # this has to be last:
    s = s.replace("&amp;", "&")
    s = s.replace("Collection of products named ", "")
    s = s.replace("Advanced Search" , "")
    s = s.replace("Verify site&#39;s SSL certificate", "")
    s = s.replace("&#39;", "")
    return s

def unescape2(s):
    s = s.replace(" ", "+")
    return s

def unescape4(s):
    s = s.replace(" ", "+")
    s = s.replace("\n", "")
    return s


def unescape5(s):
    s = s.replace(",", "")
    return s


def unescape6(s):
    s = s.replace("&apos;", "'")
    s = s.replace("&amp;", "&")
    s = s.replace('&quot;', '"')
    s = s.replace("', '",",")
    return s

#For collecting keywords and values
mydictionary = {}

#For RSS Extraction
pear = unescape2(myinput)
print(pear)
print('{:8} {:8} {:5} {:10} {:14} {:10}'.format('Watch', 'Sold', 'Hour', 'Price','ItemID','Title'))
linkforprocessing = ("http://rest.ebay.com/epn/v1/find/item.rss?keyword=" + pear + "&programid=1&campaignid=5338598285&toolid=10039&lgeo=1&descriptionSearch=true&feedType=rss&sortOrder=BestMatch&listingType1=AuctionWithBIN&listingType2=FixedPrice&minPrice=" + priceinputmin +"&maxPrice="+ priceinputmax + "&buyerPostalCode=" + zipcode + "&maxDistance=" + distancetozipcode)
f = requests.get(linkforprocessing)
websiteData = f.text
extractEbayItemIDFromWebsite = re.findall ('<guid>(.+?)</guid>', websiteData)

count = 0
for itemID in extractEbayItemIDFromWebsite:
                
    title = AnalyseAnItemIDForTitle(itemID)
    price = AnalyseItemIDForPrice(itemID)
    title = BMP(title)
    title = unescape6(title)
    title = title[0:81]
    price = unescape5(price)
    price = pricefix(price)
    price = float(price)

    mykey = title[0:20]
    myvalue = price
    mydictionary.update({mykey : myvalue})
    
    count += 1
    
    
    print ("count:",count)
    print(title[0:20],price)
    if count == limit:
        break




print('Original dictionary : ',mydictionary)
sorted_d = sorted(mydictionary.items(), key=operator.itemgetter(1))
print('Dictionary in ascending order by value : ',sorted_d)


studentsDict = dict(sorted_d)

performance = []
objects = []

for v in studentsDict.values():
    performance.append(v)

for k in studentsDict:
    objects.append(k)




#For collecting keywords and values
mydictionary2 = {}

#For RSS Extraction
pear = unescape2(myinput)
print(pear)
print('{:8} {:8} {:5} {:10} {:14} {:10}'.format('Watch', 'Sold', 'Hour', 'Price','ItemID','Title'))
linkforprocessing = ("http://rest.ebay.com/epn/v1/find/item.rss?keyword=" + pear + "&programid=1&campaignid=5338598285&toolid=10039&lgeo=1&descriptionSearch=true&feedType=rss&sortOrder=BestMatch&listingType1=AuctionWithBIN&listingType2=FixedPrice&minPrice=" + priceinputmin +"&maxPrice="+ priceinputmax + "&buyerPostalCode=" + zipcode2 + "&maxDistance=" + distancetozipcode)
f = requests.get(linkforprocessing)
websiteData = f.text
extractEbayItemIDFromWebsite = re.findall ('<guid>(.+?)</guid>', websiteData)

count2 = 0
for itemID in extractEbayItemIDFromWebsite:
                
    title = AnalyseAnItemIDForTitle(itemID)
    price = AnalyseItemIDForPrice(itemID)
    title = BMP(title)
    title = unescape6(title)
    title = title[0:81]
    price = unescape5(price)
    price = pricefix(price)
    price = float(price)

    mykey = title[0:20]
    myvalue = price
    mydictionary2.update({mykey : myvalue})
    
    count2 += 1
    
    
    print ("count:",count2)
    print(title[0:20],price)
    if count2 == limit:
        break



print('Original dictionary : ',mydictionary2)
sorted_d = sorted(mydictionary2.items(), key=operator.itemgetter(1))
print('Dictionary in ascending order by value : ',sorted_d)

studentsDict2 = dict(sorted_d)

performance2 = []
objects2 = []

for v in studentsDict2.values():
    performance2.append(v)

for k in studentsDict2:
    objects2.append(k)





#BUILDING THE COMBINED GRAPH

combinedPrice = performance2 + performance
combinedTitles = objects2 + objects

colordivider = len(performance2) - 1

y_pos = np.arange(len(combinedPrice))
barlist = plt.barh(y_pos, combinedPrice, align='center', alpha=0.5)
barlist[-1].set_color('r')
barlist[colordivider].set_color('g')
plt.yticks(y_pos, combinedTitles)
plt.xlabel('Price')
plt.title("keyword: " + myinput + "\n Zip Code:" + zipcode + " AND " + zipcode2 +  "\n Radius distance:" + distancetozipcode + " km")
plt.show()


#BUILDING THE GRAPH FIRST ZIPCODE

y_pos = np.arange(len(objects))
barlist = plt.barh(y_pos, performance, align='center', alpha=0.5)
barlist[-1].set_color('r')
plt.yticks(y_pos, objects)
plt.xlabel('Price')
plt.title("keyword: " + myinput + "\n Zip Code:" + zipcode + "\n Radius distance:" + distancetozipcode + " km")
plt.show()


#BUILDING THE GRAPH SECOND ZIPCODE

y_pos = np.arange(len(objects2))
barlist = plt.barh(y_pos, performance2, align='center', alpha=0.5)
barlist[-1].set_color('g')
plt.yticks(y_pos, objects2)
plt.xlabel('Price')
plt.title("keyword: " + myinput + "\n Zip Code:" + zipcode2 + "\n Radius distance:" + distancetozipcode + " km")
plt.show()



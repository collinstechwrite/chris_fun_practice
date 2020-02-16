import sys
import urllib
import re
from datetime import datetime
import tweepy
from twython import Twython, TwythonError
import requests
import time
from random import randint, choice, sample, randrange, shuffle
from time import sleep
from twitter import *
import os
from colorama import init, Fore, Back, Style
from io import BytesIO
from googletrans import Translator
translator = Translator()


init(convert=True)



errorcount = 0
countpromotions = 0
totalprice = 0.00
extractMostPopular = []
price = 0.00
favouritecount = 0






def pricefix(qb):

    try:
        pricef = float(qb)
        return pricef

    except Exception:

        qb = 0
        return qb
        
        



def removeap(z):
        z = z.replace(",", "")
        return z


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



#CODE FOR REMOVING UTF FORMAT
def BMP(s):
    return "".join((i if ord(i) < 10000 else '\ufffd' for i in s))

















def increment():
    global countpromotions
    global totalprice
    global price
    
    if countpromotions >= 8:
        countpromotions = 0
    countpromotions = countpromotions+1
    totalprice = totalprice + price




print("CHECKING HOT EBAY USA TRENDS")
linkforpopular = ("https://www.wuanto.com/mostwatched/allkw/0/0") #This link has hot trends of things for sale in USA
zz = requests.get(linkforpopular)
populardata = zz.text
getlistofkeywords = re.findall('href="mostwatched/(.+?)/0/0', populardata) #extract a most sold keyword


for word in getlistofkeywords:        
    extractMostPopular.append(word) 


print(extractMostPopular)



myfilelist =[]

try:
    
    fh = open('myimportfile.txt')
    for line in fh:
        # in python 2
        # print line
        # in python 3
        myfilelist.append(line)
    fh.close()

    print("MY OWN FILE LIST")
    shuffle(myfilelist)
    print(myfilelist)


except FileNotFoundError:
    sys.exit("You need to create a file called myimportfile.txt and place it in the folder with .exe")



File_save="."

def auth_any_user():
	"""	
		user authorization using pin code 
		using the library https://github.com/sixohsix/twitter 
	"""
	CONSUMER_KEY = 'ENTER YOUR OWN TWITTER DEVELOPER KEY'
	CONSUMER_SECRET = 'ENTER YOUR OWN TWITTER DEVELOPER KEY'
	name_account="1" #this will be saved in folder as .1 , delete the .1 file if you want to authenticate a new Twitter account
	File_save="."+name_account
        
	MY_TWITTER_CREDS=os.path.expanduser(File_save)



	
	#MY_TWITTER_CREDS = os.path.expanduser('~/.my_app_credentials')
	if not os.path.exists(MY_TWITTER_CREDS):
		oauth_dance("My App Name", CONSUMER_KEY, CONSUMER_SECRET,
					MY_TWITTER_CREDS)
 
	oauth_token, oauth_secret = read_token_file(MY_TWITTER_CREDS)
        

	return oauth_token, oauth_secret

print("Your Twitter authentication details are save to ", os.getcwd(), "\\" , File_save)


    
def test_send_message(ABC,itemID):
    try:
        
        print("initializing sending...")
        consumer_key = 'ENTER YOUR OWN TWITTER DEVELOPER KEY'
        consumer_secret = 'ENTER YOUR OWN TWITTER DEVELOPER KEY'
        with open(".1")as fp:
                access_token=fp.readline().strip()
                access_token_secret=fp.readline().strip()

        twitter = Twython(
                consumer_key,
                consumer_secret,
                access_token,
                access_token_secret
        )
        sleep(randint(90,200))



        linkforfindinghowmanysold = ("https://www.ebay.com/itm/" + itemID)
        h = requests.get(linkforfindinghowmanysold)
        mostsolddata = h.text
        extractMostSoldonEbay = re.findall('<meta name="twitter:image" content="https://i.ebayimg.com/images/g/(.+?).jpg" />', mostsolddata)
        extractMostSoldonEbay = extractMostSoldonEbay[0]
      

        url = "https://i.ebayimg.com/thumbs/images/g/" + extractMostSoldonEbay + ".jpg" 

        response = requests.get(url)
        photo = BytesIO(response.content)
        response = twitter.upload_media(media=photo)

        MyMessage = ABC





        twitter.update_status(status=MyMessage, media_ids=[response['media_id']])
        print("TWEET SENT") 
        
        
        """if __name__== "__main__":"""

    except Exception as ez:

        try:
        
            print("initializing sending...")
            consumer_key = 'ENTER YOUR OWN TWITTER DEVELOPER KEY'
            consumer_secret = 'ENTER YOUR OWN KEY'
            with open(".1")as fp:
                    access_token=fp.readline().strip()
                    access_token_secret=fp.readline().strip()

            twitter = Twython(
                    consumer_key,
                    consumer_secret,
                    access_token,
                    access_token_secret
            )
            sleep(randint(90,200))
            MyMessage = ABC
            twitter.update_status(status=MyMessage)
            print("TWEET SENT") 
            
            
            """if __name__== "__main__":"""

        except Exception as ez:
            print(ez)
            global errorcount
            errorcount += 1
            return errorcount



auth_any_user()




def pricefix(qb):

    try:
        pricef = float(qb)
        return pricef

    except Exception:

        qb = 0
        return qb
        
        



def removeap(z):
        z = z.replace(",", "")
        return z


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



#CODE FOR REMOVING UTF FORMAT
def BMP(s):
    return "".join((i if ord(i) < 10000 else '\ufffd' for i in s))

def ownfile():
    
    try:


        global myfilelist
        
        myset_data = []
        
        for fruit in myfilelist:


            pear = unescape2(fruit)
            print(pear)
            print('{:8} {:8} {:5} {:10} {:14} {:10}'.format('Watch', 'Sold', 'Hour', 'Price','ItemID','Title'))
            linkforprocessing = ("http://rest.ebay.com/epn/v1/find/item.rss?keyword="+ pear +"&sortOrder=BestMatch&programid=1&campaignid=5337424366&toolid=10039&minPrice="+ priceinput +".0&listingType1=All&topRatedSeller=true&feedType=rss&lgeo=1")

            f = requests.get(linkforprocessing)
             
            
            websiteData = f.text
            
            

            extractEbayItemIDFromWebsite = re.findall ('<guid>(.+?)</guid>', websiteData)




            global price
            for itemID in extractEbayItemIDFromWebsite:
            
                title = AnalyseAnItemIDForTitle(itemID)
                price = AnalyseItemIDForPrice(itemID)
                title = BMP(title)
                title = unescape6(title)
                title = title[0:81]
                price = unescape5(price)
                price = pricefix(price)
                price = float(price)
                mostSold = AnalyseAnItemID(itemID)
                mostSoldinhours = AnalyseAnItemIDForhours(itemID)
                watchers = AnalyseAnItemIDForWatchers(itemID)
                

                print('{:*^8} {:_>8} {:*^5} {:_>10.2f} {:_^14} {:_<10}'.format(watchers, mostSold, mostSoldinhours, price, itemID, title))


                if price >= float(priceinput) and watchers >= int(watchersinput) and mostSold >= int(mostSoldinput) and mostSoldinhours >= int(mostSoldinhoursvar):
                    
                    
                    global countpromotions
                    global totalprice
                    increment()
                    

                    if mostSold > 2000 and mostSoldinhours > 2:

                        if itemID in myset_data:
                            print("Skipping Duplicate")
                            break
                        myset_data.append(itemID)

                        title = str(title)
                        translation = translator.translate(title, dest=mylanguagechoice)
                        print(translation.origin, ' -> ', translation.text)
                        title = translation.text




                        
                        price = '{0:.2f}'.format(price)
                        price = str(price)
                        mostSold = str(mostSold)
                        mostSoldinhours = str(mostSoldinhours)
                        watchers = str(watchers)
                        itemID = str(itemID)

                        
                        keyword = pear
                        
                        
                        
                        

                        print("PREPARING TO TWEET ITEM ID: " + itemID + " : " + title)
                        
                        
                        
                        



                        myebayurl = "http://rover.ebay.com/rover/1/711-53200-19255-0/1?icep_ff3=2&pub=5575036718&toolid=10001&campid=" + yourebaycampaignID +"&customid=&icep_item=" + itemID + "&ipn=psmain&icep_vectorid=229466&kwid=902099&mtid=824&kw=lg"


                        

                    
                        

                        #CHECK EBAY ITEM CONVERSION URL AND MOSTSOLDINHOUR TEXT

                        
                        mystr = title
                        wordList = re.sub("[^\w]", " ",  mystr).split()

                        NEWWORDLIST = (sample(wordList, 2))

                        
                        print(Fore.RED + "SENDING TWEET")
                        
                        tag1 = NEWWORDLIST[0]
                        tag2 = NEWWORDLIST[1]

                        

                        MyRandomPhrases = ("Thousands sold","Hot Product","Trending","Selling Fast","Fantastic offer","Why wait?","Trusted seller!","Top seller!","Want","Try","Terrific","Superb","Super","Nice","Looking for","Great Deal","Give","Gift Item","Best Ever","Best","Affordable","A fabulous gift")
                        MyRandomPrices = ("Yours for","Only","Just","Buy it now!","On sale","For","Get it now","Buy now","Going for","Best price","Bargain","Selling for")
                        num = randrange(0,20)
                        num2 = randrange(0,10)


                        translation3 = translator.translate(MyRandomPhrases[num], dest=mylanguagechoice)
                        print(translation3.origin, ' -> ', translation3.text)
                        MyRandomPhrasesPublish = translation3.text



                        translation4 = translator.translate(MyRandomPrices[num2], dest=mylanguagechoice)
                        print(translation4.origin, ' -> ', translation4.text)
                        MyRandomPricesPublish = translation4.text



                        
                    
                        print(Fore.RED + "{} #{} #{} #{}, Sold over {}, {} sold in last hour. {} ${} http://rover.ebay.com/rover/1/711-53200-19255-0/1?icep_ff3=2&pub=5575036718&toolid=10001&campid={}&customid=&icep_item={}&ipn=psmain&icep_vectorid=229466&kwid=902099&mtid=824&kw=lg ".format(MyRandomPhrasesPublish,title,str(tag1),str(tag2),mostSold,mostSoldinhours,MyRandomPricesPublish,price,yourebaycampaignID,itemID))
                        ABC = ("{} #{} #{} #{}, Sold over {}, {} sold in last hour. {} ${} http://rover.ebay.com/rover/1/711-53200-19255-0/1?icep_ff3=2&pub=5575036718&toolid=10001&campid={}&customid=&icep_item={}&ipn=psmain&icep_vectorid=229466&kwid=902099&mtid=824&kw=lg ".format(MyRandomPhrasesPublish,title,str(tag1),str(tag2),mostSold,mostSoldinhours,MyRandomPricesPublish,price,yourebaycampaignID,itemID))
                        test_send_message(ABC,itemID)
                        print(Fore.WHITE + 'NEXT PROCESS')
                        print(errorcount)
                        print(countpromotions)
                        print(totalprice)

                        if errorcount >= 3:
                            sys.exit("TOO MANY ERRORS HAVE OCCURED. EXITING TWEETER. HAVE A NICE DAY! CHECK YOUR TWITTER ISN'T LOCKED. TRY AGAIN IN A FEW HOURS.")
                            
                        if countpromotions >= 7:

                            break
     


                    elif mostSold > 0 and mostSoldinhours > 0:

                        if itemID in myset_data:
                            print("Skipping Duplicate")
                            break
                        myset_data.append(itemID)



                        title = str(title)
                        translation = translator.translate(title, dest=mylanguagechoice)
                        print(translation.origin, ' -> ', translation.text)
                        title = translation.text



                        price = '{0:.2f}'.format(price)
                        price = str(price)
                        mostSold = str(mostSold)
                        mostSoldinhours = str(mostSoldinhours)
                        watchers = str(watchers)
                        itemID = str(itemID)

                        
                        keyword = pear
                        
                        
                        
                        

                        print("PREPARING TO TWEET ITEM ID: " + itemID + " : " + title)
                        
                        
                        
                        


                        myebayurl = "http://rover.ebay.com/rover/1/711-53200-19255-0/1?icep_ff3=2&pub=5575036718&toolid=10001&campid=" + yourebaycampaignID +"&customid=&icep_item=" + itemID + "&ipn=psmain&icep_vectorid=229466&kwid=902099&mtid=824&kw=lg"


                        

                    

                        #CHECK EBAY ITEM CONVERSION URL AND MOSTSOLDINHOUR TEXT

                        
                        mystr = title
                        wordList = re.sub("[^\w]", " ",  mystr).split()

                        NEWWORDLIST = (sample(wordList, 2))

                        
                        print(Fore.RED + "SENDING TWEET")
                        
                        tag1 = NEWWORDLIST[0]
                        tag2 = NEWWORDLIST[1]

                        

                        MyRandomPhrases = ("Want","Try","Terrific","Superb","Super","Nice","Looking for","Great Deal","Give","Gift Item","Best Ever","Best","Affordable","A fabulous gift")



                        
                        MyRandomPrices = ("Yours for","Only","Just","Buy it now!","On sale","For","Get it now","Buy now","Going for","Best price","Bargain","Selling for")
                        num = randrange(0,12)
                        num2 = randrange(0,10)


                        translation3 = translator.translate(MyRandomPhrases[num], dest=mylanguagechoice)
                        print(translation3.origin, ' -> ', translation3.text)
                        MyRandomPhrasesPublish = translation3.text



                        translation4 = translator.translate(MyRandomPrices[num2], dest=mylanguagechoice)
                        print(translation4.origin, ' -> ', translation4.text)
                        MyRandomPricesPublish = translation4.text




                        
                    
                        print(Fore.RED + "{} #{} #{} #{}, Sold over {}, {} sold in last hour. {} ${} http://rover.ebay.com/rover/1/711-53200-19255-0/1?icep_ff3=2&pub=5575036718&toolid=10001&campid={}&customid=&icep_item={}&ipn=psmain&icep_vectorid=229466&kwid=902099&mtid=824&kw=lg ".format(MyRandomPhrasesPublish,title,str(tag1),str(tag2),mostSold,mostSoldinhours,MyRandomPricesPublish,price,yourebaycampaignID,itemID))
                        ABC = ("{} #{} #{} #{}, Sold over {}, {} sold in last hour. {} ${} http://rover.ebay.com/rover/1/711-53200-19255-0/1?icep_ff3=2&pub=5575036718&toolid=10001&campid={}&customid=&icep_item={}&ipn=psmain&icep_vectorid=229466&kwid=902099&mtid=824&kw=lg ".format(MyRandomPhrasesPublish,title,str(tag1),str(tag2),mostSold,mostSoldinhours,MyRandomPricesPublish,price,yourebaycampaignID,itemID))
                        test_send_message(ABC,itemID)
                        print(Fore.WHITE + 'NEXT PROCESS')
                        print(errorcount)
                        print(countpromotions)
                        print(totalprice)

                        if errorcount >= 3:
                            sys.exit("TOO MANY ERRORS HAVE OCCURED. EXITING TWEETER. HAVE A NICE DAY! CHECK YOUR TWITTER ISN'T LOCKED. TRY AGAIN IN A FEW HOURS.")
                            
                        if countpromotions >= 7:

                            break
                        



                    elif mostSold == 0:

                        if "apple" or "Apple" in title:


                            if itemID in myset_data:
                                print("Skipping Duplicate")
                                break
                            myset_data.append(itemID)


                            title = str(title)
                            translation = translator.translate(title, dest=mylanguagechoice)
                            print(translation.origin, ' -> ', translation.text)
                            title = translation.text




                            price = '{0:.2f}'.format(price)
                            price = str(price)
                            mostSold = str(mostSold)
                            mostSoldinhours = str(mostSoldinhours)
                            watchers = str(watchers)
                            itemID = str(itemID)

                            
                            keyword = pear
                            
                            
                            
                            

                            print("PREPARING TO TWEET ITEM ID: " + itemID + " : " + title)
                            
                            
                            
                            

                            myebayurl = "http://rover.ebay.com/rover/1/711-53200-19255-0/1?icep_ff3=2&pub=5575036718&toolid=10001&campid=" + yourebaycampaignID +"&customid=&icep_item=" + itemID + "&ipn=psmain&icep_vectorid=229466&kwid=902099&mtid=824&kw=lg"
                            


                            
                            mystr = title
                            wordList = re.sub("[^\w]", " ",  mystr).split()

                            NEWWORDLIST = (sample(wordList, 2))

                            
                            print(Fore.RED + "SENDING TWEET")
                            
                            tag1 = NEWWORDLIST[0]
                            tag2 = NEWWORDLIST[1]
                            #RANDOM TECH PHRASES
                            MyRandomPhrases = ("Want","Try","Terrific","Superb","Super","Nice","Looking for","Great Deal","Give","Gift Item","Best Ever","Best","Affordable","A fabulous gift")



                            
                            MyRandomPrices = ("Yours for","Only","Just","Buy it now!","On sale","For","Get it now","Buy now","Going for","Best price","Bargain","Selling for")
                            num = randrange(0,12)
                            num2 = randrange(0,10)




                            translation4 = translator.translate(MyRandomPrices[num2], dest=mylanguagechoice)
                            print(translation4.origin, ' -> ', translation4.text)
                            MyRandomPricesPublish = translation4.text




                            translation3 = translator.translate(MyRandomPhrases[num], dest=mylanguagechoice)
                            print(translation3.origin, ' -> ', translation3.text)
                            MyRandomPhrasesPublish = translation3.text
                        
                            print(Fore.RED + "{} #{} #{} #{}, {} Watchers, {} ${} http://rover.ebay.com/rover/1/711-53200-19255-0/1?icep_ff3=2&pub=5575036718&toolid=10001&campid={}&customid=&icep_item={}&ipn=psmain&icep_vectorid=229466&kwid=902099&mtid=824&kw=lg ".format(MyRandomPhrasesPublish,title,str(tag1),str(tag2),watchers,MyRandomPricesPublish,price,yourebaycampaignID,itemID))
                            ABC = ("{} #{} #{} #{}, {} Watchers, {} ${} http://rover.ebay.com/rover/1/711-53200-19255-0/1?icep_ff3=2&pub=5575036718&toolid=10001&campid={}&customid=&icep_item={}&ipn=psmain&icep_vectorid=229466&kwid=902099&mtid=824&kw=lg ".format(MyRandomPhrasesPublish,title,str(tag1),str(tag2),watchers,MyRandomPricesPublish,price,yourebaycampaignID,itemID))

                            test_send_message(ABC,itemID)
                            print(Fore.WHITE + 'NEXT PROCESS')
                            print(errorcount)
                            print(countpromotions)
                            print(totalprice)


                            
                            
                            if errorcount >= 3:
                                sys.exit("TOO MANY ERRORS HAVE OCCURED. EXITING TWEETER. HAVE A NICE DAY! CHECK YOUR TWITTER ISN'T LOCKED. TRY AGAIN IN A FEW HOURS.")

                            if countpromotions >= 7:
                                
                                break
                    

                        elif "antique" or "Antique" or "antique," or "Antique," in title:


                            if itemID in myset_data:
                                print("Skipping Duplicate")
                                break
                            myset_data.append(itemID)




                            title = str(title)
                            translation = translator.translate(title, dest=mylanguagechoice)
                            print(translation.origin, ' -> ', translation.text)
                            title = translation.text



                            price = '{0:.2f}'.format(price)
                            price = str(price)
                            mostSold = str(mostSold)
                            mostSoldinhours = str(mostSoldinhours)
                            watchers = str(watchers)
                            itemID = str(itemID)

                            
                            keyword = pear
                            
                            
                            
                            


                            print("PREPARING TO TWEET ITEM ID: " + itemID + " : " + title)
                            
                            
                            
                            


                            myebayurl = "http://rover.ebay.com/rover/1/711-53200-19255-0/1?icep_ff3=2&pub=5575036718&toolid=10001&campid=" + yourebaycampaignID +"&customid=&icep_item=" + itemID + "&ipn=psmain&icep_vectorid=229466&kwid=902099&mtid=824&kw=lg"
                            
                            
                            
                            mystr = title
                            wordList = re.sub("[^\w]", " ",  mystr).split()

                            NEWWORDLIST = (sample(wordList, 2))

                            
                            print(Fore.RED + "SENDING TWEET")
                            
                            tag1 = NEWWORDLIST[0]
                            tag2 = NEWWORDLIST[1]


                            #RANDOM ANTIQUE
                            MyRandomPhrases = ("Rare","Collectable","Fine","Great find","Collector peice","Seeking","Looking for","Great Deal","Give","Gift Item","Best Ever","Best","Affordable","A fabulous gift")




                            
                            MyRandomPrices = ("Yours for","Only","Just","Buy it now!","On sale","For","Get it now","Buy now","Going for","Best price","Bargain","Selling for")
                            num = randrange(0,12)
                            num2 = randrange(0,10)


                            translation3 = translator.translate(MyRandomPhrases[num], dest=mylanguagechoice)
                            print(translation3.origin, ' -> ', translation3.text)
                            MyRandomPhrasesPublish = translation3.text






                            translation4 = translator.translate(MyRandomPrices[num2], dest=mylanguagechoice)
                            print(translation4.origin, ' -> ', translation4.text)
                            MyRandomPricesPublish = translation4.text






                            print(Fore.RED + "{} #{} #{} #{}, {} Watchers, {} ${} http://rover.ebay.com/rover/1/711-53200-19255-0/1?icep_ff3=2&pub=5575036718&toolid=10001&campid={}&customid=&icep_item={}&ipn=psmain&icep_vectorid=229466&kwid=902099&mtid=824&kw=lg ".format(MyRandomPhrasesPublish,title,str(tag1),str(tag2),watchers,MyRandomPricesPublish,price,yourebaycampaignID,itemID))
                            ABC = ("{} #{} #{} #{}, {} Watchers, {} ${} http://rover.ebay.com/rover/1/711-53200-19255-0/1?icep_ff3=2&pub=5575036718&toolid=10001&campid={}&customid=&icep_item={}&ipn=psmain&icep_vectorid=229466&kwid=902099&mtid=824&kw=lg ".format(MyRandomPhrasesPublish,title,str(tag1),str(tag2),watchers,MyRandomPricesPublish,price,yourebaycampaignID,itemID))

                            test_send_message(ABC,itemID)
                            print(Fore.WHITE + 'NEXT PROCESS')
                            print(errorcount)
                            print(countpromotions)
                            print(totalprice)
  
                            if errorcount >= 3:
                                sys.exit("TOO MANY ERRORS HAVE OCCURED. EXITING TWEETER. HAVE A NICE DAY! CHECK YOUR TWITTER ISN'T LOCKED. TRY AGAIN IN A FEW HOURS.")

                            if countpromotions >= 7:
                                
                                break

                        
                        else:


                            if itemID in myset_data:
                                print("Skipping Duplicate")
                                break
                            myset_data.append(itemID)



                            title = str(title)
                            translation = translator.translate(title, dest=mylanguagechoice)
                            print(translation.origin, ' -> ', translation.text)
                            title = translation.text



                            price = '{0:.2f}'.format(price)
                            price = str(price)
                            mostSold = str(mostSold)
                            mostSoldinhours = str(mostSoldinhours)
                            watchers = str(watchers)
                            itemID = str(itemID)

                            
                            keyword = pear
                            
                            
                            
                            



                            print("PREPARING TO TWEET ITEM ID: " + itemID + " : " + title)
                            
                            
                            
                            


                            
                            

                            myebayurl = "http://rover.ebay.com/rover/1/711-53200-19255-0/1?icep_ff3=2&pub=5575036718&toolid=10001&campid=" + yourebaycampaignID +"&customid=&icep_item=" + itemID + "&ipn=psmain&icep_vectorid=229466&kwid=902099&mtid=824&kw=lg"

                            
                        
                            
                            
                            mystr = title
                            wordList = re.sub("[^\w]", " ",  mystr).split()

                            NEWWORDLIST = (sample(wordList, 2))

                            
                            print(Fore.RED + "SENDING TWEET")
                            
                            tag1 = NEWWORDLIST[0]
                            tag2 = NEWWORDLIST[1]



                            MyRandomPhrases = ("Want","Try","Terrific","Superb","Super","Nice","Looking for","Great Deal","Give","Gift Item","Best Ever","Best","Affordable","A fabulous gift")



                            
                            MyRandomPrices = ("Yours for","Only","Just","Buy it now!","On sale","For","Get it now","Buy now","Going for","Best price","Bargain","Selling for")
                            num = randrange(0,12)
                            num2 = randrange(0,10)




                            translation4 = translator.translate(MyRandomPrices[num2], dest=mylanguagechoice)
                            print(translation4.origin, ' -> ', translation4.text)
                            MyRandomPricesPublish = translation4.text





                            translation3 = translator.translate(MyRandomPhrases[num], dest=mylanguagechoice)
                            print(translation3.origin, ' -> ', translation3.text)
                            MyRandomPhrasesPublish = translation3.text
                            
                            print(Fore.RED + "{} #{} #{} #{}, {} Watchers, {} ${} http://rover.ebay.com/rover/1/711-53200-19255-0/1?icep_ff3=2&pub=5575036718&toolid=10001&campid={}&customid=&icep_item={}&ipn=psmain&icep_vectorid=229466&kwid=902099&mtid=824&kw=lg ".format(MyRandomPhrasesPublish,title,str(tag1),str(tag2),watchers,MyRandomPricesPublish,price,yourebaycampaignID,itemID))
                            ABC = ("{} #{} #{} #{}, {} Watchers, {} ${} http://rover.ebay.com/rover/1/711-53200-19255-0/1?icep_ff3=2&pub=5575036718&toolid=10001&campid={}&customid=&icep_item={}&ipn=psmain&icep_vectorid=229466&kwid=902099&mtid=824&kw=lg ".format(MyRandomPhrasesPublish,title,str(tag1),str(tag2),watchers,MyRandomPricesPublish,price,yourebaycampaignID,itemID))

                            test_send_message(ABC,itemID)
                            print(Fore.WHITE + 'NEXT PROCESS')
                            print(errorcount)
                            print(countpromotions)
                            print(totalprice)

                            if errorcount >= 3:
                                sys.exit("TOO MANY ERRORS HAVE OCCURED. EXITING TWEETER. HAVE A NICE DAY! CHECK YOUR TWITTER ISN'T LOCKED. TRY AGAIN IN A FEW HOURS.")

                            if countpromotions >= 7:
                                
                                break

                    elif mostSold >= 0 and mostSoldinhours  == 0:


                        if itemID in myset_data:
                            print("Skipping Duplicate")
                            break
                        myset_data.append(itemID)

                        

                        title = str(title)
                        translation = translator.translate(title, dest=mylanguagechoice)
                        print(translation.origin, ' -> ', translation.text)
                        title = translation.text



                        price = '{0:.2f}'.format(price)
                        price = str(price)
                        mostSold = str(mostSold)
                        mostSoldinhours = str(mostSoldinhours)
                        watchers = str(watchers)
                        itemID = str(itemID)

                        
                        keyword = pear
                        
                        
                        
                        


                        print("PREPARING TO TWEET ITEM ID: " + itemID + " : " + title)
                        
                        
                        
                        

                        myebayurl = "http://rover.ebay.com/rover/1/711-53200-19255-0/1?icep_ff3=2&pub=5575036718&toolid=10001&campid=" + yourebaycampaignID +"&customid=&icep_item=" + itemID + "&ipn=psmain&icep_vectorid=229466&kwid=902099&mtid=824&kw=lg"


                        

                    

                        #CHECK EBAY ITEM CONVERSION URL AND MOSTSOLDINHOUR TEXT

                        
                        mystr = title
                        wordList = re.sub("[^\w]", " ",  mystr).split()

                        NEWWORDLIST = (sample(wordList, 2))

                        
                        print(Fore.RED + "SENDING TWEET")
                        
                        tag1 = NEWWORDLIST[0]
                        tag2 = NEWWORDLIST[1]

                        MyRandomPhrases = (myhashtags + "Want","Try","Terrific","Superb","Super","Nice","Looking for","Great Deal","Give","Gift Item","Best Ever","Best","Affordable","A fabulous gift")
                        num = randrange(0,13)


                        translation3 = translator.translate(MyRandomPhrases[num], dest=mylanguagechoice)
                        print(translation3.origin, ' -> ', translation3.text)
                        MyRandomPhrasesPublish = translation3.text
                        
                    
                        print(Fore.RED + "{} #{} #{} #{}, {} Watchers, http://rover.ebay.com/rover/1/711-53200-19255-0/1?icep_ff3=2&pub=5575036718&toolid=10001&campid={}&customid=&icep_item={}&ipn=psmain&icep_vectorid=229466&kwid=902099&mtid=824&kw=lg ".format(MyRandomPhrasesPublish,title,str(tag1),str(tag2),watchers,yourebaycampaignID,itemID))
                        ABC = ("{} #{} #{} #{}, {} Watchers, http://rover.ebay.com/rover/1/711-53200-19255-0/1?icep_ff3=2&pub=5575036718&toolid=10001&campid={}&customid=&icep_item={}&ipn=psmain&icep_vectorid=229466&kwid=902099&mtid=824&kw=lg ".format(MyRandomPhrasesPublish,title,str(tag1),str(tag2),watchers,yourebaycampaignID,itemID))
                        test_send_message(ABC,itemID)
                        print(Fore.WHITE + 'NEXT PROCESS')

                        print(errorcount)
                        print(countpromotions)
                        print(totalprice)
                        
                        if errorcount >= 3:
                            sys.exit("TOO MANY ERRORS HAVE OCCURED. EXITING TWEETER. HAVE A NICE DAY! CHECK YOUR TWITTER ISN'T LOCKED. TRY AGAIN IN A FEW HOURS.")
                        

                        if countpromotions >= 7:

                            break
                                            
                    
                    elif mostSold == 0 and mostSoldinhours  == 0:


                        if itemID in myset_data:
                            print("Skipping Duplicate")
                            break
                        myset_data.append(itemID)
                        
                        title = str(title)
                        translation = translator.translate(title, dest=mylanguagechoice)
                        print(translation.origin, ' -> ', translation.text)
                        title = translation.text


                        
                        price = '{0:.2f}'.format(price)
                        price = str(price)
                        mostSold = str(mostSold)
                        mostSoldinhours = str(mostSoldinhours)
                        watchers = str(watchers)
                        itemID = str(itemID)

                        
                        keyword = pear
                        
                        
                        
                        


                        print("PREPARING TO TWEET ITEM ID: " + itemID + " : " + title)
                        
                        
                        
                        

                        myebayurl = "http://rover.ebay.com/rover/1/711-53200-19255-0/1?icep_ff3=2&pub=5575036718&toolid=10001&campid=" + yourebaycampaignID +"&customid=&icep_item=" + itemID + "&ipn=psmain&icep_vectorid=229466&kwid=902099&mtid=824&kw=lg"


                        

                        #CHECK EBAY ITEM CONVERSION URL AND MOSTSOLDINHOUR TEXT

                        
                        mystr = title
                        wordList = re.sub("[^\w]", " ",  mystr).split()

                        NEWWORDLIST = (sample(wordList, 2))

                        
                        print(Fore.RED + "SENDING TWEET")
                        
                        tag1 = NEWWORDLIST[0]
                        tag2 = NEWWORDLIST[1]

                        MyRandomPhrases = ("Want","Try","Terrific","Superb","Super","Nice","Looking for","Great Deal","Give","Gift Item","Best Ever","Best","Affordable","A fabulous gift")




                        num = randrange(0,13)


                        translation3 = translator.translate(MyRandomPhrases[num], dest=mylanguagechoice)
                        print(translation3.origin, ' -> ', translation3.text)
                        MyRandomPhrasesPublish = translation3.text

                        
                    
                        print(Fore.RED + "{} #{} #{} #{}, {} Watchers, http://rover.ebay.com/rover/1/711-53200-19255-0/1?icep_ff3=2&pub=5575036718&toolid=10001&campid={}&customid=&icep_item={}&ipn=psmain&icep_vectorid=229466&kwid=902099&mtid=824&kw=lg ".format(MyRandomPhrasesPublish,title,str(tag1),str(tag2),watchers,yourebaycampaignID,itemID))
                        ABC = ("{} #{} #{} #{}, {} Watchers, http://rover.ebay.com/rover/1/711-53200-19255-0/1?icep_ff3=2&pub=5575036718&toolid=10001&campid={}&customid=&icep_item={}&ipn=psmain&icep_vectorid=229466&kwid=902099&mtid=824&kw=lg ".format(MyRandomPhrasesPublish,title,str(tag1),str(tag2),watchers,yourebaycampaignID,itemID))
                        test_send_message(ABC,itemID)
                        print(Fore.WHITE + 'NEXT PROCESS')

                        print(errorcount)
                        print(countpromotions)
                        print(totalprice)
                        
                        if errorcount >= 3:
                            sys.exit("TOO MANY ERRORS HAVE OCCURED. EXITING TWEETER. HAVE A NICE DAY! CHECK YOUR TWITTER ISN'T LOCKED. TRY AGAIN IN A FEW HOURS.")
                        

                        if countpromotions >= 7:

                            break
                        

        
           
                    else:

                        if itemID in myset_data:
                            print("Skipping Duplicate")
                            break
                        myset_data.append(itemID)
            
                        title = str(title)
                        translation = translator.translate(title, dest=mylanguagechoice)
                        print(translation.origin, ' -> ', translation.text)
                        title = translation.text




                        
                        price = '{0:.2f}'.format(price)
                        price = str(price)
                        mostSold = str(mostSold)
                        mostSoldinhours = str(mostSoldinhours)
                        watchers = str(watchers)
                        itemID = str(itemID)

                        
                        keyword = pear
                        
                        
                        
                        

                        print("PREPARING TO TWEET ITEM ID: " + itemID + " : " + title)
                        
                        
                        
                        

                        myebayurl = "http://rover.ebay.com/rover/1/711-53200-19255-0/1?icep_ff3=2&pub=5575036718&toolid=10001&campid=" + yourebaycampaignID +"&customid=&icep_item=" + itemID + "&ipn=psmain&icep_vectorid=229466&kwid=902099&mtid=824&kw=lg"

                        

                        #CHECK EBAY ITEM CONVERSION URL AND MOSTSOLDINHOUR TEXT

                        mystr = title
                        wordList = re.sub("[^\w]", " ",  mystr).split()

                        NEWWORDLIST = (sample(wordList, 2))

                        
                        print(Fore.RED + "SENDING TWEET")
                        
                        tag1 = NEWWORDLIST[0]
                        tag2 = NEWWORDLIST[1]
                        



                        MyRandomPhrases = ("Want","Try","Terrific","Superb","Super","Nice","Looking for","Great Deal","Give","Gift Item","Best Ever","Best","Affordable","A fabulous gift")

                        
                        num = randrange(0,12)


                        translation3 = translator.translate(MyRandomPhrases[num], dest=mylanguagechoice)
                        print(translation3.origin, ' -> ', translation3.text)
                        MyRandomPhrasesPublish = translation3.text

                    
                        print(Fore.RED + "{} #{} #{} #{}, Sold over {}, {} sold in last hour http://rover.ebay.com/rover/1/711-53200-19255-0/1?icep_ff3=2&pub=5575036718&toolid=10001&campid={}&customid=&icep_item={}&ipn=psmain&icep_vectorid=229466&kwid=902099&mtid=824&kw=lg ".format(MyRandomPhrasesPublish,title,str(tag1),str(tag2),mostSold,mostSoldinhours,yourebaycampaignID,itemID))
                        ABC = ("{} #{} #{} #{}, Sold over {}, {} sold in last hour http://rover.ebay.com/rover/1/711-53200-19255-0/1?icep_ff3=2&pub=5575036718&toolid=10001&campid={}&customid=&icep_item={}&ipn=psmain&icep_vectorid=229466&kwid=902099&mtid=824&kw=lg ".format(MyRandomPhrasesPublish,title,str(tag1),str(tag2),mostSold,mostSoldinhours,yourebaycampaignID,itemID))
                        test_send_message(ABC,itemID)
                        print(Fore.WHITE + 'NEXT PROCESS')

                        print(errorcount)
                        print(countpromotions)
                        print(totalprice)

                        if errorcount >= 3:
                            sys.exit("TOO MANY ERRORS HAVE OCCURED. EXITING TWEETER. HAVE A NICE DAY! CHECK YOUR TWITTER ISN'T LOCKED. TRY AGAIN IN A FEW HOURS.")

                        if countpromotions >= 7:

                            break
    except Exception as ex:
        print(ex)
        print("MOVING TO NEXT PROCESS")
        pass




def MyEbayTestCode():
    try:
        global extractMostPopular
        global priceinput
        
        
        myset_data = []
        
        for fruit in extractMostPopular:

            pear = unescape2(fruit)
            print(pear)
            print('{:8} {:8} {:5} {:10} {:14} {:10}'.format('Watch', 'Sold', 'Hour', 'Price','ItemID','Title'))
            linkforprocessing = ("http://rest.ebay.com/epn/v1/find/item.rss?keyword="+ pear +"&sortOrder=BestMatch&programid=1&campaignid=5337424366&toolid=10039&minPrice="+ priceinput +".0&listingType1=All&topRatedSeller=true&feedType=rss&lgeo=1")

            f = requests.get(linkforprocessing)
             
            
            websiteData = f.text
            
            

            extractEbayItemIDFromWebsite = re.findall ('<guid>(.+?)</guid>', websiteData)



            global price
            for itemID in extractEbayItemIDFromWebsite:
            
                title = AnalyseAnItemIDForTitle(itemID)
                price = AnalyseItemIDForPrice(itemID)
                title = BMP(title)
                title = unescape6(title)
                title = title[0:81]
                price = unescape5(price)
                price = pricefix(price)
                price = float(price)
                mostSold = AnalyseAnItemID(itemID)
                mostSoldinhours = AnalyseAnItemIDForhours(itemID)
                watchers = AnalyseAnItemIDForWatchers(itemID)
                

                print('{:*^8} {:_>8} {:*^5} {:_>10.2f} {:_^14} {:_<10}'.format(watchers, mostSold, mostSoldinhours, price, itemID, title))


                if price >= float(priceinput) and watchers >= int(watchersinput) and mostSold >= int(mostSoldinput) and mostSoldinhours >= int(mostSoldinhoursvar):
                    
                    
                    global countpromotions
                    global totalprice
                    increment()
                    

                    if mostSold > 2000 and mostSoldinhours > 2:

                        if itemID in myset_data:
                            print("Skipping Duplicate")
                            break
                        myset_data.append(itemID)

                        title = str(title)
                        translation = translator.translate(title, dest=mylanguagechoice)
                        print(translation.origin, ' -> ', translation.text)
                        title = translation.text




                        
                        price = '{0:.2f}'.format(price)
                        price = str(price)
                        mostSold = str(mostSold)
                        mostSoldinhours = str(mostSoldinhours)
                        watchers = str(watchers)
                        itemID = str(itemID)

                        
                        keyword = pear
                        
                        
                        
                        

                        print("PREPARING TO TWEET ITEM ID: " + itemID + " : " + title)
                        
                        
                        
                        



                        myebayurl = "http://rover.ebay.com/rover/1/711-53200-19255-0/1?icep_ff3=2&pub=5575036718&toolid=10001&campid=" + yourebaycampaignID +"&customid=&icep_item=" + itemID + "&ipn=psmain&icep_vectorid=229466&kwid=902099&mtid=824&kw=lg"


                        

                    
                        

                        #CHECK EBAY ITEM CONVERSION URL AND MOSTSOLDINHOUR TEXT

                        
                        mystr = title
                        wordList = re.sub("[^\w]", " ",  mystr).split()

                        NEWWORDLIST = (sample(wordList, 2))

                        
                        print(Fore.RED + "SENDING TWEET")
                        
                        tag1 = NEWWORDLIST[0]
                        tag2 = NEWWORDLIST[1]

                        

                        MyRandomPhrases = ("Thousands sold","Hot Product","Trending","Selling Fast","Fantastic offer","Why wait?","Trusted seller!","Top seller!","Want","Try","Terrific","Superb","Super","Nice","Looking for","Great Deal","Give","Gift Item","Best Ever","Best","Affordable","A fabulous gift")
                        MyRandomPrices = ("Yours for","Only","Just","Buy it now!","On sale","For","Get it now","Buy now","Going for","Best price","Bargain","Selling for")
                        num = randrange(0,20)
                        num2 = randrange(0,10)


                        translation3 = translator.translate(MyRandomPhrases[num], dest=mylanguagechoice)
                        print(translation3.origin, ' -> ', translation3.text)
                        MyRandomPhrasesPublish = translation3.text



                        translation4 = translator.translate(MyRandomPrices[num2], dest=mylanguagechoice)
                        print(translation4.origin, ' -> ', translation4.text)
                        MyRandomPricesPublish = translation4.text



                        
                    
                        print(Fore.RED + "{} #{} #{} #{}, Sold over {}, {} sold in last hour. {} ${} http://rover.ebay.com/rover/1/711-53200-19255-0/1?icep_ff3=2&pub=5575036718&toolid=10001&campid={}&customid=&icep_item={}&ipn=psmain&icep_vectorid=229466&kwid=902099&mtid=824&kw=lg ".format(MyRandomPhrasesPublish,title,str(tag1),str(tag2),mostSold,mostSoldinhours,MyRandomPricesPublish,price,yourebaycampaignID,itemID))
                        ABC = ("{} #{} #{} #{}, Sold over {}, {} sold in last hour. {} ${} http://rover.ebay.com/rover/1/711-53200-19255-0/1?icep_ff3=2&pub=5575036718&toolid=10001&campid={}&customid=&icep_item={}&ipn=psmain&icep_vectorid=229466&kwid=902099&mtid=824&kw=lg ".format(MyRandomPhrasesPublish,title,str(tag1),str(tag2),mostSold,mostSoldinhours,MyRandomPricesPublish,price,yourebaycampaignID,itemID))
                        test_send_message(ABC,itemID)
                        print(Fore.WHITE + 'NEXT PROCESS')
                        print(errorcount)
                        print(countpromotions)
                        print(totalprice)

                        if errorcount >= 3:
                            sys.exit("TOO MANY ERRORS HAVE OCCURED. EXITING TWEETER. HAVE A NICE DAY! CHECK YOUR TWITTER ISN'T LOCKED. TRY AGAIN IN A FEW HOURS.")
                            
                        if countpromotions >= 7:

                            break
     


                    elif mostSold > 0 and mostSoldinhours > 0:

                        if itemID in myset_data:
                            print("Skipping Duplicate")
                            break
                        myset_data.append(itemID)



                        title = str(title)
                        translation = translator.translate(title, dest=mylanguagechoice)
                        print(translation.origin, ' -> ', translation.text)
                        title = translation.text



                        price = '{0:.2f}'.format(price)
                        price = str(price)
                        mostSold = str(mostSold)
                        mostSoldinhours = str(mostSoldinhours)
                        watchers = str(watchers)
                        itemID = str(itemID)

                        
                        keyword = pear
                        
                        
                        
                        

                        print("PREPARING TO TWEET ITEM ID: " + itemID + " : " + title)
                        
                        
                        
                        


                        myebayurl = "http://rover.ebay.com/rover/1/711-53200-19255-0/1?icep_ff3=2&pub=5575036718&toolid=10001&campid=" + yourebaycampaignID +"&customid=&icep_item=" + itemID + "&ipn=psmain&icep_vectorid=229466&kwid=902099&mtid=824&kw=lg"


                        

                    

                        #CHECK EBAY ITEM CONVERSION URL AND MOSTSOLDINHOUR TEXT

                        
                        mystr = title
                        wordList = re.sub("[^\w]", " ",  mystr).split()

                        NEWWORDLIST = (sample(wordList, 2))

                        
                        print(Fore.RED + "SENDING TWEET")
                        
                        tag1 = NEWWORDLIST[0]
                        tag2 = NEWWORDLIST[1]

                        

                        MyRandomPhrases = ("Want","Try","Terrific","Superb","Super","Nice","Looking for","Great Deal","Give","Gift Item","Best Ever","Best","Affordable","A fabulous gift")



                        
                        MyRandomPrices = ("Yours for","Only","Just","Buy it now!","On sale","For","Get it now","Buy now","Going for","Best price","Bargain","Selling for")
                        num = randrange(0,12)
                        num2 = randrange(0,10)


                        translation3 = translator.translate(MyRandomPhrases[num], dest=mylanguagechoice)
                        print(translation3.origin, ' -> ', translation3.text)
                        MyRandomPhrasesPublish = translation3.text



                        translation4 = translator.translate(MyRandomPrices[num2], dest=mylanguagechoice)
                        print(translation4.origin, ' -> ', translation4.text)
                        MyRandomPricesPublish = translation4.text




                        
                    
                        print(Fore.RED + "{} #{} #{} #{}, Sold over {}, {} sold in last hour. {} ${} http://rover.ebay.com/rover/1/711-53200-19255-0/1?icep_ff3=2&pub=5575036718&toolid=10001&campid={}&customid=&icep_item={}&ipn=psmain&icep_vectorid=229466&kwid=902099&mtid=824&kw=lg ".format(MyRandomPhrasesPublish,title,str(tag1),str(tag2),mostSold,mostSoldinhours,MyRandomPricesPublish,price,yourebaycampaignID,itemID))
                        ABC = ("{} #{} #{} #{}, Sold over {}, {} sold in last hour. {} ${} http://rover.ebay.com/rover/1/711-53200-19255-0/1?icep_ff3=2&pub=5575036718&toolid=10001&campid={}&customid=&icep_item={}&ipn=psmain&icep_vectorid=229466&kwid=902099&mtid=824&kw=lg ".format(MyRandomPhrasesPublish,title,str(tag1),str(tag2),mostSold,mostSoldinhours,MyRandomPricesPublish,price,yourebaycampaignID,itemID))
                        test_send_message(ABC,itemID)
                        print(Fore.WHITE + 'NEXT PROCESS')
                        print(errorcount)
                        print(countpromotions)
                        print(totalprice)

                        if errorcount >= 3:
                            sys.exit("TOO MANY ERRORS HAVE OCCURED. EXITING TWEETER. HAVE A NICE DAY! CHECK YOUR TWITTER ISN'T LOCKED. TRY AGAIN IN A FEW HOURS.")
                            
                        if countpromotions >= 7:

                            break
                        



                    elif mostSold == 0:

                        if "apple" or "Apple" in title:


                            if itemID in myset_data:
                                print("Skipping Duplicate")
                                break
                            myset_data.append(itemID)


                            title = str(title)
                            translation = translator.translate(title, dest=mylanguagechoice)
                            print(translation.origin, ' -> ', translation.text)
                            title = translation.text




                            price = '{0:.2f}'.format(price)
                            price = str(price)
                            mostSold = str(mostSold)
                            mostSoldinhours = str(mostSoldinhours)
                            watchers = str(watchers)
                            itemID = str(itemID)

                            
                            keyword = pear
                            
                            
                            
                            

                            print("PREPARING TO TWEET ITEM ID: " + itemID + " : " + title)
                            
                            
                            
                            

                            myebayurl = "http://rover.ebay.com/rover/1/711-53200-19255-0/1?icep_ff3=2&pub=5575036718&toolid=10001&campid=" + yourebaycampaignID +"&customid=&icep_item=" + itemID + "&ipn=psmain&icep_vectorid=229466&kwid=902099&mtid=824&kw=lg"
                            


                            
                            mystr = title
                            wordList = re.sub("[^\w]", " ",  mystr).split()

                            NEWWORDLIST = (sample(wordList, 2))

                            
                            print(Fore.RED + "SENDING TWEET")
                            
                            tag1 = NEWWORDLIST[0]
                            tag2 = NEWWORDLIST[1]
                            #RANDOM TECH PHRASES
                            MyRandomPhrases = ("Want","Try","Terrific","Superb","Super","Nice","Looking for","Great Deal","Give","Gift Item","Best Ever","Best","Affordable","A fabulous gift")



                            
                            MyRandomPrices = ("Yours for","Only","Just","Buy it now!","On sale","For","Get it now","Buy now","Going for","Best price","Bargain","Selling for")
                            num = randrange(0,12)
                            num2 = randrange(0,10)




                            translation4 = translator.translate(MyRandomPrices[num2], dest=mylanguagechoice)
                            print(translation4.origin, ' -> ', translation4.text)
                            MyRandomPricesPublish = translation4.text




                            translation3 = translator.translate(MyRandomPhrases[num], dest=mylanguagechoice)
                            print(translation3.origin, ' -> ', translation3.text)
                            MyRandomPhrasesPublish = translation3.text
                        
                            print(Fore.RED + "{} #{} #{} #{}, {} Watchers, {} ${} http://rover.ebay.com/rover/1/711-53200-19255-0/1?icep_ff3=2&pub=5575036718&toolid=10001&campid={}&customid=&icep_item={}&ipn=psmain&icep_vectorid=229466&kwid=902099&mtid=824&kw=lg ".format(MyRandomPhrasesPublish,title,str(tag1),str(tag2),watchers,MyRandomPricesPublish,price,yourebaycampaignID,itemID))
                            ABC = ("{} #{} #{} #{}, {} Watchers, {} ${} http://rover.ebay.com/rover/1/711-53200-19255-0/1?icep_ff3=2&pub=5575036718&toolid=10001&campid={}&customid=&icep_item={}&ipn=psmain&icep_vectorid=229466&kwid=902099&mtid=824&kw=lg ".format(MyRandomPhrasesPublish,title,str(tag1),str(tag2),watchers,MyRandomPricesPublish,price,yourebaycampaignID,itemID))

                            test_send_message(ABC,itemID)
                            print(Fore.WHITE + 'NEXT PROCESS')
                            print(errorcount)
                            print(countpromotions)
                            print(totalprice)


                            
                            
                            if errorcount >= 3:
                                sys.exit("TOO MANY ERRORS HAVE OCCURED. EXITING TWEETER. HAVE A NICE DAY! CHECK YOUR TWITTER ISN'T LOCKED. TRY AGAIN IN A FEW HOURS.")

                            if countpromotions >= 7:
                                
                                break
                    

                        elif "antique" or "Antique" or "antique," or "Antique," in title:


                            if itemID in myset_data:
                                print("Skipping Duplicate")
                                break
                            myset_data.append(itemID)




                            title = str(title)
                            translation = translator.translate(title, dest=mylanguagechoice)
                            print(translation.origin, ' -> ', translation.text)
                            title = translation.text



                            price = '{0:.2f}'.format(price)
                            price = str(price)
                            mostSold = str(mostSold)
                            mostSoldinhours = str(mostSoldinhours)
                            watchers = str(watchers)
                            itemID = str(itemID)

                            
                            keyword = pear
                            
                            
                            
                            


                            print("PREPARING TO TWEET ITEM ID: " + itemID + " : " + title)
                            
                            
                            
                            


                            myebayurl = "http://rover.ebay.com/rover/1/711-53200-19255-0/1?icep_ff3=2&pub=5575036718&toolid=10001&campid=" + yourebaycampaignID +"&customid=&icep_item=" + itemID + "&ipn=psmain&icep_vectorid=229466&kwid=902099&mtid=824&kw=lg"
                            
                            
                            
                            mystr = title
                            wordList = re.sub("[^\w]", " ",  mystr).split()

                            NEWWORDLIST = (sample(wordList, 2))

                            
                            print(Fore.RED + "SENDING TWEET")
                            
                            tag1 = NEWWORDLIST[0]
                            tag2 = NEWWORDLIST[1]


                            #RANDOM ANTIQUE
                            MyRandomPhrases = ("Rare","Collectable","Fine","Great find","Collector peice","Seeking","Looking for","Great Deal","Give","Gift Item","Best Ever","Best","Affordable","A fabulous gift")




                            
                            MyRandomPrices = ("Yours for","Only","Just","Buy it now!","On sale","For","Get it now","Buy now","Going for","Best price","Bargain","Selling for")
                            num = randrange(0,12)
                            num2 = randrange(0,10)


                            translation3 = translator.translate(MyRandomPhrases[num], dest=mylanguagechoice)
                            print(translation3.origin, ' -> ', translation3.text)
                            MyRandomPhrasesPublish = translation3.text






                            translation4 = translator.translate(MyRandomPrices[num2], dest=mylanguagechoice)
                            print(translation4.origin, ' -> ', translation4.text)
                            MyRandomPricesPublish = translation4.text






                            print(Fore.RED + "{} #{} #{} #{}, {} Watchers, {} ${} http://rover.ebay.com/rover/1/711-53200-19255-0/1?icep_ff3=2&pub=5575036718&toolid=10001&campid={}&customid=&icep_item={}&ipn=psmain&icep_vectorid=229466&kwid=902099&mtid=824&kw=lg ".format(MyRandomPhrasesPublish,title,str(tag1),str(tag2),watchers,MyRandomPricesPublish,price,yourebaycampaignID,itemID))
                            ABC = ("{} #{} #{} #{}, {} Watchers, {} ${} http://rover.ebay.com/rover/1/711-53200-19255-0/1?icep_ff3=2&pub=5575036718&toolid=10001&campid={}&customid=&icep_item={}&ipn=psmain&icep_vectorid=229466&kwid=902099&mtid=824&kw=lg ".format(MyRandomPhrasesPublish,title,str(tag1),str(tag2),watchers,MyRandomPricesPublish,price,yourebaycampaignID,itemID))

                            test_send_message(ABC,itemID)
                            print(Fore.WHITE + 'NEXT PROCESS')
                            print(errorcount)
                            print(countpromotions)
                            print(totalprice)
  
                            if errorcount >= 3:
                                sys.exit("TOO MANY ERRORS HAVE OCCURED. EXITING TWEETER. HAVE A NICE DAY! CHECK YOUR TWITTER ISN'T LOCKED. TRY AGAIN IN A FEW HOURS.")

                            if countpromotions >= 7:
                                
                                break

                        
                        else:


                            if itemID in myset_data:
                                print("Skipping Duplicate")
                                break
                            myset_data.append(itemID)



                            title = str(title)
                            translation = translator.translate(title, dest=mylanguagechoice)
                            print(translation.origin, ' -> ', translation.text)
                            title = translation.text



                            price = '{0:.2f}'.format(price)
                            price = str(price)
                            mostSold = str(mostSold)
                            mostSoldinhours = str(mostSoldinhours)
                            watchers = str(watchers)
                            itemID = str(itemID)

                            keyword = pear




                            print("PREPARING TO TWEET ITEM ID: " + itemID + " : " + title)


                            myebayurl = "http://rover.ebay.com/rover/1/711-53200-19255-0/1?icep_ff3=2&pub=5575036718&toolid=10001&campid=" + yourebaycampaignID +"&customid=&icep_item=" + itemID + "&ipn=psmain&icep_vectorid=229466&kwid=902099&mtid=824&kw=lg"

                            
                        
                            
                            
                            mystr = title
                            wordList = re.sub("[^\w]", " ",  mystr).split()

                            NEWWORDLIST = (sample(wordList, 2))

                            
                            print(Fore.RED + "SENDING TWEET")
                            
                            tag1 = NEWWORDLIST[0]
                            tag2 = NEWWORDLIST[1]



                            MyRandomPhrases = ("Want","Try","Terrific","Superb","Super","Nice","Looking for","Great Deal","Give","Gift Item","Best Ever","Best","Affordable","A fabulous gift")



                            
                            MyRandomPrices = ("Yours for","Only","Just","Buy it now!","On sale","For","Get it now","Buy now","Going for","Best price","Bargain","Selling for")
                            num = randrange(0,12)
                            num2 = randrange(0,10)




                            translation4 = translator.translate(MyRandomPrices[num2], dest=mylanguagechoice)
                            print(translation4.origin, ' -> ', translation4.text)
                            MyRandomPricesPublish = translation4.text





                            translation3 = translator.translate(MyRandomPhrases[num], dest=mylanguagechoice)
                            print(translation3.origin, ' -> ', translation3.text)
                            MyRandomPhrasesPublish = translation3.text
                            
                            print(Fore.RED + "{} #{} #{} #{}, {} Watchers, {} ${} http://rover.ebay.com/rover/1/711-53200-19255-0/1?icep_ff3=2&pub=5575036718&toolid=10001&campid={}&customid=&icep_item={}&ipn=psmain&icep_vectorid=229466&kwid=902099&mtid=824&kw=lg ".format(MyRandomPhrasesPublish,title,str(tag1),str(tag2),watchers,MyRandomPricesPublish,price,yourebaycampaignID,itemID))
                            ABC = ("{} #{} #{} #{}, {} Watchers, {} ${} http://rover.ebay.com/rover/1/711-53200-19255-0/1?icep_ff3=2&pub=5575036718&toolid=10001&campid={}&customid=&icep_item={}&ipn=psmain&icep_vectorid=229466&kwid=902099&mtid=824&kw=lg ".format(MyRandomPhrasesPublish,title,str(tag1),str(tag2),watchers,MyRandomPricesPublish,price,yourebaycampaignID,itemID))

                            test_send_message(ABC,itemID)
                            print(Fore.WHITE + 'NEXT PROCESS')
                            print(errorcount)
                            print(countpromotions)
                            print(totalprice)

                            if errorcount >= 3:
                                sys.exit("TOO MANY ERRORS HAVE OCCURED. EXITING TWEETER. HAVE A NICE DAY! CHECK YOUR TWITTER ISN'T LOCKED. TRY AGAIN IN A FEW HOURS.")

                            if countpromotions >= 7:
                                
                                break

                    elif mostSold >= 0 and mostSoldinhours  == 0:


                        if itemID in myset_data:
                            print("Skipping Duplicate")
                            break
                        myset_data.append(itemID)

                        

                        title = str(title)
                        translation = translator.translate(title, dest=mylanguagechoice)
                        print(translation.origin, ' -> ', translation.text)
                        title = translation.text



                        price = '{0:.2f}'.format(price)
                        price = str(price)
                        mostSold = str(mostSold)
                        mostSoldinhours = str(mostSoldinhours)
                        watchers = str(watchers)
                        itemID = str(itemID)


                        keyword = pear



                        print("PREPARING TO TWEET ITEM ID: " + itemID + " : " + title)


                        myebayurl = "http://rover.ebay.com/rover/1/711-53200-19255-0/1?icep_ff3=2&pub=5575036718&toolid=10001&campid=" + yourebaycampaignID +"&customid=&icep_item=" + itemID + "&ipn=psmain&icep_vectorid=229466&kwid=902099&mtid=824&kw=lg"


                        

                    

                        #CHECK EBAY ITEM CONVERSION URL AND MOSTSOLDINHOUR TEXT

                        
                        mystr = title
                        wordList = re.sub("[^\w]", " ",  mystr).split()

                        NEWWORDLIST = (sample(wordList, 2))

                        
                        print(Fore.RED + "SENDING TWEET")
                        
                        tag1 = NEWWORDLIST[0]
                        tag2 = NEWWORDLIST[1]

                        MyRandomPhrases = (myhashtags + "Want","Try","Terrific","Superb","Super","Nice","Looking for","Great Deal","Give","Gift Item","Best Ever","Best","Affordable","A fabulous gift")
                        num = randrange(0,13)


                        translation3 = translator.translate(MyRandomPhrases[num], dest=mylanguagechoice)
                        print(translation3.origin, ' -> ', translation3.text)
                        MyRandomPhrasesPublish = translation3.text
                        
                    
                        print(Fore.RED + "{} #{} #{} #{}, {} Watchers, http://rover.ebay.com/rover/1/711-53200-19255-0/1?icep_ff3=2&pub=5575036718&toolid=10001&campid={}&customid=&icep_item={}&ipn=psmain&icep_vectorid=229466&kwid=902099&mtid=824&kw=lg ".format(MyRandomPhrasesPublish,title,str(tag1),str(tag2),watchers,yourebaycampaignID,itemID))
                        ABC = ("{} #{} #{} #{}, {} Watchers, http://rover.ebay.com/rover/1/711-53200-19255-0/1?icep_ff3=2&pub=5575036718&toolid=10001&campid={}&customid=&icep_item={}&ipn=psmain&icep_vectorid=229466&kwid=902099&mtid=824&kw=lg ".format(MyRandomPhrasesPublish,title,str(tag1),str(tag2),watchers,yourebaycampaignID,itemID))
                        test_send_message(ABC,itemID)
                        print(Fore.WHITE + 'NEXT PROCESS')

                        print(errorcount)
                        print(countpromotions)
                        print(totalprice)
                        
                        if errorcount >= 3:
                            sys.exit("TOO MANY ERRORS HAVE OCCURED. EXITING TWEETER. HAVE A NICE DAY! CHECK YOUR TWITTER ISN'T LOCKED. TRY AGAIN IN A FEW HOURS.")
                        

                        if countpromotions >= 7:

                            break
                                            
                    
                    elif mostSold == 0 and mostSoldinhours  == 0:


                        if itemID in myset_data:
                            print("Skipping Duplicate")
                            break
                        myset_data.append(itemID)
                        
                        title = str(title)
                        translation = translator.translate(title, dest=mylanguagechoice)
                        print(translation.origin, ' -> ', translation.text)
                        title = translation.text


                        
                        price = '{0:.2f}'.format(price)
                        price = str(price)
                        mostSold = str(mostSold)
                        mostSoldinhours = str(mostSoldinhours)
                        watchers = str(watchers)
                        itemID = str(itemID)

                        keyword = pear

                        print("PREPARING TO TWEET ITEM ID: " + itemID + " : " + title)


                        myebayurl = "http://rover.ebay.com/rover/1/711-53200-19255-0/1?icep_ff3=2&pub=5575036718&toolid=10001&campid=" + yourebaycampaignID +"&customid=&icep_item=" + itemID + "&ipn=psmain&icep_vectorid=229466&kwid=902099&mtid=824&kw=lg"


                        #CHECK EBAY ITEM CONVERSION URL AND MOSTSOLDINHOUR TEXT

                        
                        mystr = title
                        wordList = re.sub("[^\w]", " ",  mystr).split()

                        NEWWORDLIST = (sample(wordList, 2))

                        
                        print(Fore.RED + "SENDING TWEET")
                        
                        tag1 = NEWWORDLIST[0]
                        tag2 = NEWWORDLIST[1]

                        MyRandomPhrases = ("Want","Try","Terrific","Superb","Super","Nice","Looking for","Great Deal","Give","Gift Item","Best Ever","Best","Affordable","A fabulous gift")




                        num = randrange(0,13)


                        translation3 = translator.translate(MyRandomPhrases[num], dest=mylanguagechoice)
                        print(translation3.origin, ' -> ', translation3.text)
                        MyRandomPhrasesPublish = translation3.text

                        
                    
                        print(Fore.RED + "{} #{} #{} #{}, {} Watchers, http://rover.ebay.com/rover/1/711-53200-19255-0/1?icep_ff3=2&pub=5575036718&toolid=10001&campid={}&customid=&icep_item={}&ipn=psmain&icep_vectorid=229466&kwid=902099&mtid=824&kw=lg ".format(MyRandomPhrasesPublish,title,str(tag1),str(tag2),watchers,yourebaycampaignID,itemID))
                        ABC = ("{} #{} #{} #{}, {} Watchers, http://rover.ebay.com/rover/1/711-53200-19255-0/1?icep_ff3=2&pub=5575036718&toolid=10001&campid={}&customid=&icep_item={}&ipn=psmain&icep_vectorid=229466&kwid=902099&mtid=824&kw=lg ".format(MyRandomPhrasesPublish,title,str(tag1),str(tag2),watchers,yourebaycampaignID,itemID))
                        test_send_message(ABC,itemID)
                        print(Fore.WHITE + 'NEXT PROCESS')

                        print(errorcount)
                        print(countpromotions)
                        print(totalprice)
                        
                        if errorcount >= 3:
                            sys.exit("TOO MANY ERRORS HAVE OCCURED. EXITING TWEETER. HAVE A NICE DAY! CHECK YOUR TWITTER ISN'T LOCKED. TRY AGAIN IN A FEW HOURS.")
                        

                        if countpromotions >= 7:

                            break
                        

        
           
                    else:

                        if itemID in myset_data:
                            print("Skipping Duplicate")
                            break
                        myset_data.append(itemID)
            
                        title = str(title)
                        translation = translator.translate(title, dest=mylanguagechoice)
                        print(translation.origin, ' -> ', translation.text)
                        title = translation.text




                        
                        price = '{0:.2f}'.format(price)
                        price = str(price)
                        mostSold = str(mostSold)
                        mostSoldinhours = str(mostSoldinhours)
                        watchers = str(watchers)
                        itemID = str(itemID)

                        keyword = pear


                        print("PREPARING TO TWEET ITEM ID: " + itemID + " : " + title)
 
                        myebayurl = "http://rover.ebay.com/rover/1/711-53200-19255-0/1?icep_ff3=2&pub=5575036718&toolid=10001&campid=" + yourebaycampaignID +"&customid=&icep_item=" + itemID + "&ipn=psmain&icep_vectorid=229466&kwid=902099&mtid=824&kw=lg"

                        

                        #CHECK EBAY ITEM CONVERSION URL AND MOSTSOLDINHOUR TEXT

                        mystr = title
                        wordList = re.sub("[^\w]", " ",  mystr).split()

                        NEWWORDLIST = (sample(wordList, 2))

                        
                        print(Fore.RED + "SENDING TWEET")
                        
                        tag1 = NEWWORDLIST[0]
                        tag2 = NEWWORDLIST[1]
                        



                        MyRandomPhrases = ("Want","Try","Terrific","Superb","Super","Nice","Looking for","Great Deal","Give","Gift Item","Best Ever","Best","Affordable","A fabulous gift")

                        
                        num = randrange(0,12)


                        translation3 = translator.translate(MyRandomPhrases[num], dest=mylanguagechoice)
                        print(translation3.origin, ' -> ', translation3.text)
                        MyRandomPhrasesPublish = translation3.text

                    
                        print(Fore.RED + "{} #{} #{} #{}, Sold over {}, {} sold in last hour http://rover.ebay.com/rover/1/711-53200-19255-0/1?icep_ff3=2&pub=5575036718&toolid=10001&campid={}&customid=&icep_item={}&ipn=psmain&icep_vectorid=229466&kwid=902099&mtid=824&kw=lg ".format(MyRandomPhrasesPublish,title,str(tag1),str(tag2),mostSold,mostSoldinhours,yourebaycampaignID,itemID))
                        ABC = ("{} #{} #{} #{}, Sold over {}, {} sold in last hour http://rover.ebay.com/rover/1/711-53200-19255-0/1?icep_ff3=2&pub=5575036718&toolid=10001&campid={}&customid=&icep_item={}&ipn=psmain&icep_vectorid=229466&kwid=902099&mtid=824&kw=lg ".format(MyRandomPhrasesPublish,title,str(tag1),str(tag2),mostSold,mostSoldinhours,yourebaycampaignID,itemID))
                        test_send_message(ABC,itemID)
                        print(Fore.WHITE + 'NEXT PROCESS')

                        print(errorcount)
                        print(countpromotions)
                        print(totalprice)

                        if errorcount >= 3:
                            sys.exit("TOO MANY ERRORS HAVE OCCURED. EXITING TWEETER. HAVE A NICE DAY! CHECK YOUR TWITTER ISN'T LOCKED. TRY AGAIN IN A FEW HOURS.")

                        if countpromotions >= 7:

                            break
    except Exception as ex:
        print(ex)
        print("MOVING TO NEXT PROCESS")
        pass


LANGUAGES = {
    'ar': 'arabic', #encoding issue
    'zh-cn': 'chinese (simplified)', #encoding issue
    'zh-tw': 'chinese (traditional)', #encoding issue
    'da': 'danish', #wealthy
    'nl': 'dutch', #wealthy
    'en': 'english', #wealthy
    'fi': 'finnish', #wealthy
    'fr': 'french', #wealthy
    'de': 'german', #wealthy
    'it': 'italian', #wealthy
    'ja': 'japanese', #wealthy
    'lb': 'luxembourgish', #wealthy
    'ms': 'malay', #wealthy
    'ro': 'romanian', #wealthy
    'sv': 'swedish', #wealthy
    'ta': 'tamil', #wealthy
}


yourebaycampaignID = input("Input your eBay CampaignID Number:")
while len(yourebaycampaignID) < 10:
    
    if yourebaycampaignID == "":
        print("eBay CampaignID == NULL, default campaignID 5338595494 will be used")
        yourebaycampaignID = "5338595494"
        break

    elif len(yourebaycampaignID) < 10:
        print("It appears you have made an error, check length of your ebay campaign ID")
        yourebaycampaignID = input("Input your eBay CampaignID Number:")

print("Your ebay campaign ID is:", yourebaycampaignID) 

 


priceinput = input("Enter your minimum price:__make this high to selectively post high ticket items to increase commission payments__don't be greedy :)")
watchersinput = input ("Enter minimum watchers__remember watch counts can be faked__but its good to have items with a lot of interest__")
mostSoldinput = input("Enter minimum most sold__sales really indicate an items popularity__enter minimum past sales__")
mostSoldinhoursvar = input("Enter minimum amount sold recently__")
myhashtags = input("Enter a single hashtag, it will be randomised with Call to actions e.g #TopOffer")



print('{:8} {:5} {:10} {:14} {:10}'.format(mostSoldinput, mostSoldinhoursvar, priceinput,'ItemID','Title'))





choose = input("Do you want to use hot trends from the internet? - YES \n Or upload your own file? - OWN")

while choose != "YES" or "OWN":
    if choose == "YES":
        for mylanguagechoice in LANGUAGES.keys():
            print(mylanguagechoice)
            MyEbayTestCode()

        

    elif choose == "OWN":
        for mylanguagechoice in LANGUAGES.keys():
            print(mylanguagechoice)
            ownfile()

    else:
        choose = input("Do you want to use hot trends from the internet? - YES \n Or upload your own file? - OWN")

















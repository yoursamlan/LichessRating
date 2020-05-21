#Lichess Rating List Generator
#Amlan Saha Kundu
#=========================================================

import requests,io,datetime
from bs4 import BeautifulSoup
from itertools import islice
from heapq import nlargest

#Initializing Month and Year for Monthly Rank

x = datetime.datetime.now()
month = x.strftime("%b")
year = x.strftime("%Y")

#Username List

ulist = ['bhaluu','atanu','Joyotu_senior','kimkortobyobimurah','Julkifol','Subhendu519','rakibalhsn','Tirtha_Ch','cyborg18','Daniel_Rozario','Imran_Shorif_Shuvo','Samadarshi']

print("Collecting Data...")
#Data Collection
for i in range(len(ulist)):
        username = ulist[i]
        URLstring ="https://lichess.org/@/"+username
        
        print(URLstring)
        
        URL = URLstring
        headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
        html_page = requests.get(URL).text
        soup = BeautifulSoup (html_page, 'lxml')
        uname = username
        '''
        for item in soup.findAll('span', attrs={'class': 'offline user-link'}):
                #txt.write(str(item.text.strip())+"\n")
                uname = (item.text.strip())
                print(uname)
        #Creating Offline Backup
        '''
        file = uname + ".txt"
        open(file, "w").close()
        with io.open(file, "w",encoding="utf-8") as txt:
            txt.write(uname)
            for item in soup.findAll('a', attrs={'class': 'game'}):
                if item.text.strip()[:5] != 'Ultra':
                        txt.write("\n"+str(item.text.strip()))
                        #print(item.text.strip())
        txt.close()
print("Saved offline backup SUCCESSFULLY")
#Initialize Dictionary

bullet_rating = {}
blitz_rating = {}
rapid_rating = {}
classical_rating = {}

#Extract Data

for i in range(len(ulist)):
        username = ulist[i]
        filename = username + ".txt"
                
        with open(filename) as fin:
            for line in islice(fin, 1,2):
                bullet = (line[6:11])

                
        with open(filename) as fin:
            for line in islice(fin, 2,3):
                blitz = (line[5:10])

        with open(filename) as fin:
            for line in islice(fin, 3,4):
                rapid = (line[5:10])

        with open(filename) as fin:
            for line in islice(fin, 4,5):
                classical = (line[9:14])


#Add to Dictionary
                
        try:
                bullet_rating[username]= int(bullet)
        except ValueError:
                bullet_rating[username]= 0
        try:
                blitz_rating[username]= int(blitz)
        except ValueError:
                blitz_rating[username]= 0
        try:
                rapid_rating[username]= int(rapid)
        except ValueError:
                rapid_rating[username]= 0
        try:
                classical_rating[username]= int(classical)
        except ValueError:
                classical_rating[username]= 0


#Ranking List Generation

#print(bullet_rating)
                
top_bullet = nlargest(5,bullet_rating, key = bullet_rating.get)

print("\nTop 5 Bullet Player for "+month+" ,"+year)
print("-"*36)
for i in range (5):
        print(str(i+1)+". "+str(top_bullet[i])+" ("+str(bullet_rating.get(str(top_bullet[i])))+")")

#print(blitz_rating)
                
top_blitz = nlargest(5,blitz_rating, key = blitz_rating.get)

print("\nTop 5 Blitz Player for "+month+" ,"+year)
print("-"*36)
for i in range (5):
        print(str(i+1)+". "+str(top_blitz[i])+" ("+str(blitz_rating.get(str(top_blitz[i])))+")")

#print(rapid_rating)
                
top_rapid = nlargest(5,rapid_rating, key = rapid_rating.get)

print("\nTop 5 Rapid Player for "+month+" ,"+year)
print("-"*36)
for i in range (5):
        print(str(i+1)+". "+str(top_rapid[i])+" ("+str(rapid_rating.get(str(top_rapid[i])))+")")

#print(classical_rating)
                
top_classical = nlargest(5,classical_rating, key = classical_rating.get)

print("\nTop 5 classical Player for "+month+" ,"+year)
print("-"*36)
for i in range (5):
        print(str(i+1)+". "+str(top_classical[i])+" ("+str(classical_rating.get(str(top_classical[i])))+")")




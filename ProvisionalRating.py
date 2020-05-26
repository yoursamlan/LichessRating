import requests,io,datetime,os
from bs4 import BeautifulSoup
from itertools import islice

#Initializing Month and Year for Monthly Rank

x = datetime.datetime.now()
month = x.strftime("%b")
year = x.strftime("%Y")

#Creating directory for backup files
flag = 0
while flag==0:
        try:
                os.chdir("BackUp"+str(x)[:10])
                flag = flag+1
        except:
                os.mkdir("BackUp"+str(x)[:10])


name = input("Enter Lichess Username: ")

print("Collecting Data...\n")
#Data Collection

URLstring ="https://lichess.org/@/"+name
print(URLstring)
URL = URLstring
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
html_page = requests.get(URL).text
soup = BeautifulSoup (html_page, 'lxml')
'''
for item in soup.findAll('span', attrs={'class': 'offline user-link'}):
        #txt.write(str(item.text.strip())+"\n")
        uname = (item.text.strip())
        print(uname)
#Creating Offline Backup
'''
file = name + ".bak"
open(file, "w").close()
with io.open(file, "w",encoding="utf-8") as txt:
    txt.write(name)
    for item in soup.findAll('a', attrs={'class': 'game'}):
        if item.text.strip()[:5] != 'Ultra':
                txt.write("\n"+str(item.text.strip()))
                #print(item.text.strip())
txt.close()
print("\nSaved offline backup SUCCESSFULLY\n")

#Extract Data


filename = name + ".bak"
        
with open(filename) as fin:
    for line in islice(fin, 1,2):
        try:
                bullet = int(line[6:11])
        except ValueError:
                bullet = 0

        
with open(filename) as fin:
    for line in islice(fin, 2,3):
        try:
                blitz = int(line[5:10])
        except ValueError:
                blitz = 0

with open(filename) as fin:
    for line in islice(fin, 3,4):
        try:
                rapid = int(line[5:10])
        except ValueError:
                rapid = 0

with open(filename) as fin:
    for line in islice(fin, 4,5):
        try:
                classical = int(line[9:14])
        except ValueError:
                classical = 0

                
if bullet!=0 and blitz!=0 and rapid != 0:
        raw_per = (2*bullet+3*blitz+5*rapid)/10
elif bullet!=0 and blitz!=0 and classical != 0:
        raw_per = (2*bullet+3*blitz+5*classical)/10
elif bullet !=0 and blitz!=0 and (rapid == 0 or classical==0) :
        raw_per = (3*bullet+5*blitz)/8
else:
        raw_per = 0

if raw_per <=1500:
        margin = 50
elif raw_per <=1700:
        margin = 75
elif raw_per <=2000:
        margin = 100
elif raw_per <=2200:
        margin = 125
elif raw_per <=2500:
        margin = 100
elif raw_per >2500:
        margin = 75

perf = raw_per - margin

if perf < 0:
        performance = "Please play at least 15 games EACH in Bullet,Blitz and Rapid to evaluate."
        fide = "N/A"
elif perf>0 and perf<2000:
        performance = perf
        fide = perf * 0.886
else:
        performance = perf
        fide = perf * 0.96


print("Bullet : "+str(bullet))
print("Blitz : "+str(blitz))
print("Rapid : "+str(rapid))
print("Classical : "+str(classical))
print("Performance: "+str(performance))
print("FIDE eq. Rating: "+str(fide))

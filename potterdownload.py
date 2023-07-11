from pathlib import Path
import os
import requests
import re
from bs4 import BeautifulSoup
import threading
directory = Path.cwd()
stem = "https://hpaudiobooks.co/"
data = [
["Sorcerer's Stone", "jim-dale-hp-1-harry-potter-and-the-sorcerers-stone/", 5],
["Chamber of Secrets","hp-2-harry-potter-chamber-secrets-jim-dale-audio-book/",5],
["Prisoner of Azkaban","audiobook-hp-3-harry-potter-prisoner-azkaban-jim-dale/", 6],
["Goblet of Fire","goblet-of-fire-jim-dale-harry-potter-hp-audio-book-4/", 10],
["Order of the Phoenix", "potter-order-phoenix-5-jim-dale-book/",10],
["Half Blood Prince", "hp-6-harry-potter-half-blood-prince-by-jim-dale-book/",8],
["Deathly Hallows", "7-harry-potter-deathly-hallow-jim-dale-book/", 10]
]
def makefolders(bookname, number, pages, baselink):
    for i in range(1,pages+1):
        r=requests.get(f'{baselink}{i}/')
        soup = BeautifulSoup(r.content, 'html.parser')
        for a in soup.find_all('a', href=re.compile(r'http.*\.mp3')):
            k = str(a)
            beglink = k.find(">")+1
            endlink = k[1:].find("<")+1
            k=k[beglink:endlink]
            filename = k.split("/")[-1].replace("%20"," ")
            r = requests.get(k)
            currpath = f"Book {number} - {bookname}"
            if not os.path.exists(currpath):
                os.makedirs(currpath)
            with open(os.path.join(currpath, filename), 'wb') as temp_file:
                temp_file.write(r.content)
t0 = threading.Thread(target=makefolders, args=(data[0][0], 1, data[0][2], stem+data[0][1]))
t1 = threading.Thread(target=makefolders, args=(data[1][0], 2, data[1][2], stem+data[1][1]))
t2 = threading.Thread(target=makefolders, args=(data[2][0], 3, data[2][2], stem+data[2][1]))
t3 = threading.Thread(target=makefolders, args=(data[3][0], 4, data[3][2], stem+data[3][1]))
t4 = threading.Thread(target=makefolders, args=(data[4][0], 5, data[4][2], stem+data[4][1]))
t5 = threading.Thread(target=makefolders, args=(data[5][0], 6, data[5][2], stem+data[5][1]))
t6 = threading.Thread(target=makefolders, args=(data[6][0], 7, data[6][2], stem+data[6][1]))
t0.start()
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()

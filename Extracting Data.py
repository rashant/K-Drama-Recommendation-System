import requests
from bs4 import BeautifulSoup
import csv
try:
    for pageno in range(1,63):
        r = requests.get(f'https://www.viki.com/v1/explore?page={pageno}')

        # Parsing the HTML
        soup = BeautifulSoup(r.content, 'html.parser')

        s = soup.find_all('a', class_='thumb-title strong')
        for id,title in enumerate(s):
            print(id+1,title.text.strip(),title.get('href'))
            url='https://www.viki.com/'+title.get('href')

            r = requests.get('https://mydramalist.com/search?q= '+title.text.strip())

            # Parsing the HTML
            soup = BeautifulSoup(r.content, 'html.parser')

            s = soup.find('h6', class_='text-primary title')
            a=s.find('a')
            surl='https://mydramalist.com'+a.get('href')
            r=requests.get(surl)
            soup = BeautifulSoup(r.content, 'html.parser')

            s=soup.find('div',class_='show-synopsis')
            p=s.find('p')
            text=p.text.strip()
            text=text.split('(Source: ')
            text=text[0]
            text=text.replace('\n',' ')
            text=text.replace('”','"')
            text=text.replace('“','"')
            text=text.replace('\r','')
            text=text.replace("’","'")
            text=text.strip()
            data=[title.text.strip(),text]
            with open('Dataset.csv','a',newline='', encoding="utf-8") as f:
                writer=csv.writer(f)
                writer.writerow(data)
except:
    pass

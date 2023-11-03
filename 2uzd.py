""" 
Iegūt ziņas, izmantojot RSS plūsmu no google.lv.

"""

import feedparser

rss_url="https://news.google.com/home?hl=lv&gl=LV&ceid=LV:lv"


kkk=feedparser.parse(rss_url)

for entry in kkk.entries:
    print("Virsraksts", entry.title)
    print("saite", entry.link
    
    )
    print("\n")
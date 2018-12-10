
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  10 22:24:08 2018

@author: KRIS
"""

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import wikipedia

path='filepath/WikiContent.txt' ###write your file path here
WikiSearch = "Rick and Morty"
####  incase you want to extract urlWise then comment Line 15 and uncomment Line 17 and 18
#wikiurl= 'https://en.wikipedia.org/wiki/Rick_and_Morty'
#WikiSearch = wikiurl[30:]
p = wikipedia.page(WikiSearch)
#print(p.content[2])
content=''
for i in p.title:
	try:
		content=content+str(i)
	except:
		pass
content = content + '\n\n'		
for i in p.content:
	try:
		content=content+str(i)
	except:
		pass

ContentFile = open(path,'w')
ContentFile.write(content)
ContentFile.close()

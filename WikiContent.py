
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  10 22:24:08 2018

@author: KRIS
"""

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import wikipedia

path='filepath/WikiContent.txt' ###write your file path here
WikiSearch = "green herb"
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

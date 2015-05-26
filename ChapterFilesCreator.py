# -*- coding: utf-8 -*-

import os, re, codecs, re

ChapterRegex = r'\W{0,3}([IVX]+)\W{0,6}$'
ChapterTitle = ""
ChapterOpen = False #le but est de savoir si chapitre est déjà ouvert
LineCounter = 0


f = open('test.txt', 'r', encoding='utf8')


for line in f.readlines():
    LineCounter += 1
    if re.search(ChapterRegex, line) != None:
        if ChapterOpen == True:
            # on ferme l'écriture du chaptire précédent
            fo.close()
            ChapterOpen=False
        if ChapterOpen == False:
            ChapterTitle = re.search(ChapterRegex, line).group(1)
            ChapterOpen = True
            print(line)
            print('NEW CHAPTER ON LINE', LineCounter, '-->', ChapterTitle)
            fo = open('%s.txt' % ChapterTitle, "a+", encoding="utf8")
            fo.write(line)
    else:
        if ChapterOpen == True:
            fo.write(line)

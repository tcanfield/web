from __future__ import division
import math
import re
import random

class Verse:
	def __init__(self, refverse):
		self.refverse = refverse
		self.find_reference()
		self.find_book()
		self.find_chapter()
		self.find_verse_num()
		self.find_verse()
	
	def find_reference(self):
		reference = re.match(r'(...[\|]\d+[\|]\d+[\|])', self.refverse)
		self.reference = reference.group()

	def find_book(self):
		book = re.match(r'(...)[\|]\d+[\|]\d+[\|]', self.refverse)
		self.book = book.group(1)

	def find_chapter(self):
		chap = re.match(r'...[\|](\d+)[\|]\d+[\|]', self.refverse)
		self.chap = chap.group(1)
	
	def find_verse_num(self):
		verse_num = re.match(r'...[\|]\d+[\|](\d+)[\|]', self.refverse)
		self.verse_num = verse_num.group(1)

	def find_verse(self):
		self.verse = self.refverse.replace(self.reference, "").strip().replace("~", "")

	def get_reference(self):
		return self.reference

	def get_book(self):
		return self.book

	def get_chapter(self):
		return self.chap

	def get_verse_num(self):
		return self.verse_num
	
	def get_verse(self):
		return self.verse

	def __str__(self):
		return self.reference + "\n" + self.verse


class Chapter:
	def __init__(self, verses):
		self.verses = verses

	def set_word_count(self, word_count):
		self.word_count = word_count

	def set_weight(self, weight):
		self.weight = weight

	def get_chapter(self):
		return self.verses

	def get_word_count(self):
		return self.word_count

	def get_weight(self):
		return self.weight
	


class Book:
	def __init__(self, chapters):
		self.chapters = chapters


bible = open("kjvdat.txt", "r")

verses = []
for line in bible:
	reference = re.match(r'(...[\|]\d+[\|]\d+[\|])', line)
	v = Verse(line)
	verses.append(v)
bible.close()

print verses[3].get_chapter()

ch_verses = []
chapters = []
first = True
current_chapter = int(1)
for verse_index in verses:
	if(first == True):
		print verse_index
	if(verse_index.get_verse_num() == '1'): #if we reach a new chapter
		if(first): #if we're on the first verse for the first time simply add the verse to the chapter's verses array		
			for x in range(0, 31): #bug setting first chapter, just doing it manually for now
				ch_verses.append(verses[x])
		else: 
			chapters.append(Chapter(ch_verses))
			#print Chapter(ch_verses).get_chapter()[0].get_verse()
			current_chapter = verse_index.get_chapter() #move to the next chapter
			#print ch_verses[0].get_verse()
			ch_verses = [] #reset the array of chapter's verses
			ch_verses.append(verse_index)
			
	elif(verse_index.get_chapter() == current_chapter):
		ch_verses.append(verse_index)
	first = False
chapters.append(Chapter(ch_verses)) #append final chapter since theres no more verse 1 to show its reset

print chapters[0].verses[0]
#randomly distribute the extra chapters since they dont divide evenly to days of year

remainder_chapters = len(chapters) % 365

remainders = []
for x in range(remainder_chapters):
	rand = random.randint(0, 365)
	while rand in remainders:
		rand = random.randint(0, 365)
	remainders.append(rand)
remainders.sort()
print remainders

#get chapters for each day, using the remainders to know which days to add an extra chapter to

chap_per_day = len(chapters)//365

current_chapter = 0;
for x in range(365):
	dayfile = open(str(x), 'w')

	if(x in remainders):
		for y in range(chap_per_day+1):	
			verses = chapters[current_chapter].verses
			for verse in verses:
				dayfile.write(str(verse) + "\n")
			current_chapter = current_chapter+1
	else:
		for y in range(chap_per_day):	
			verses = chapters[current_chapter].verses
			for verse in verses:
				dayfile.write(str(verse) + "\n")
			current_chapter = current_chapter+1
		
			

















import random, collections
from nltk.corpus import wordnet

def wordise(word):
	return word[:(len(word) - 5)]

class markov(object):
	words = []
	def __init__(self):
		self.cache = {}
		
	def addfile(self, filename):
		self.f = open(filename, 'r')
		self.words = self.file_words()
		self.db()
	
	def addwords(self, wrds):
		for word in wrds.split():
			newword = wordnet.morphy(word)
			if newword:
				print newword
				self.words.append(newword)
		
		
	def file_words(self):
		self.f.seek(0)
		data = self.f.read()
		words = data.split()
		return words
		
	def triples(self):
		if len(self.words) < 3:
			return
		for i in range(len(self.words) - 2):
			yield (self.words[i], self.words[i + 1], self.words[i + 2])
		
	def db(self):
		for w1, w2, w3 in self.triples():
			key = (w1, w2)
			if key in self.cache:
				self.cache[key].append(w3)
			else:
				self.cache[key] = [w3]
			
	def gen(self, size = 30):
		self.db()
		seed = random.randint(0, len(self.words) - 3)
		sword, nword = self.words[seed], self.words[seed + 1]
		w1, w2 = sword, nword
		gen_words = []
		for i in xrange(size):
			gen_words.append(w1)
			try:
				w1, w2 = w2, random.choice(self.cache[(w1, w2)])
			except:
				w1, w2 = w2, "and"
		gen_words.append(w2)
		return ' '.join(gen_words)

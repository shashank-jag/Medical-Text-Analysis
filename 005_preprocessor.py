import nltk
from copy import deepcopy

wordVocab = {}
posVocab = {}
nerVocab = {}

def init():
	fi=open("posVocab.txt",'r').read();
	l=fi.split()
	#print(l)
	for x in l:
		posVocab[x]=0
	fi=open("vocab.txt",'r').read();
	l=fi.split()
	for x in l:
		wordVocab[x]=0
	fi=open("nerVocab.txt",'r').read();
	l=fi.split()
	for x in l:
		nerVocab[x]=0

def getNewDic():
	ret = {}
	ret["pos"]=deepcopy(posVocab)#.deepcopy()
	ret["vocab"]=deepcopy(wordVocab)#.deepcopy()
	ret["ner"]=deepcopy(nerVocab)#.deepcop()
	return ret


def taggerPro(s):
	ret=getNewDic()
	for x in nltk.word_tokenize(s):
		try :
			ret["vocab"][x]+=1
		except :
			pass
	s=nltk.word_tokenize(s)
	pos = nltk.pos_tag(s)
#	print(pos)

	for x in pos:
		try:
			ret["pos"][x[1]]+=1
		except:
			pass
#	print(nltk.ne_chunk(pos))
	
	for chunk in nltk.ne_chunk(pos) :
		if hasattr(chunk, 'label'):
#		         print(chunk.label(), ' '.join(c[0] for c in chunk))
			try:
				ret["ner"][chunk.label()]+=1
			except:
				pass
	return ret

init()

#...................................demo
x=taggerPro("I'm learning NLP")
print(x["pos"])
print(x["ner"])
#for a in x["pos"]:
#	print(x["pos"][a],end=' ')
y=taggerPro("I'm learning ML")

#....................................dimentions

size = len(x["vocab"].keys()) + len(x["ner"].keys()) + len(x["pos"].keys())
print(size)


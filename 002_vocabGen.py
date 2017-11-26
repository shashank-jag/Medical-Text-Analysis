import os
import nltk

#os.chdir("./txt")
l=os.listdir("./txt")
#print(l)

vocab = {}

for fi in l:
	if fi[-4:] == ".txt" :
		file_content = open("./txt/"+fi,'r').read()
		tokens = nltk.word_tokenize(file_content)
		for t in tokens:
			vocab[t]=1
		print(fi,"********done")

wri = open("vocab.txt","w")
for key in vocab.keys():
	wri.write(key+'\n')
wri.close()

import subprocess
import os.path
import fcntl
import nltk
import sys

data = open("DischargeSummary/"+sys.argv[1],'r').read() 
data = data.lower()

complete_data = data

data = data.replace('\n',' ')
data = nltk.sent_tokenize(data)

#data.replace('\n',' ')

#print(data)

path_to_genia = "/home/guestdsac/qwerty/shashank/geniatagger-3.0.2"

os.chdir(path_to_genia)

#dir_to_tagger = os.path.dirname(path_to_genia)

#tagger = subprocess.call("ls",shell=True)
tagger = subprocess.Popen("./geniatagger",stdin=subprocess.PIPE, stdout=subprocess.PIPE)
#print(tagger)

results = []

#wr = open("Clean/genia_tagged_"+sys.argv[1],'w+')

#span
span = 0


#print("*********")
for oneline in data:
	tagger.stdin.write((oneline+'\n').encode('utf-8'))
	tagger.stdin.flush()
	#print('0')
	#print(oneline)
	#print(span)
	while (True):
		try :
			r = tagger.stdout.readline()[:-1]
		except : 
			continue
	#	print("****************")
	#	print(r)
		r=r.decode('utf-8')
		#r=r.replace('[ ]*',' ')
		
	#	print(r.split('\t'))
		#results.append(r.split('\\t'))
		r=r.split('\t')
		#print(r)
		#if len(r) < 5 :
		#	continue
		
		while r[0] != complete_data[span:span+len(r[0])] and span<len(complete_data):
			span+=1
	
		#print(len(r),r)
		if len(r) > 4 and len(r[1]) > 2 :
			s = str(span) + " " + str(span+len(r[0])) + '|'
			span += len(r[0])
			for x in r:
				s+=x+'|'
			s = s[:-1]	
			print(str(s))
			#wr.write(str(s))
		if len(r) == 1 and len(r[0]) ==0 :
			break
#print(results)
#print("Im mad")
#wr.close()

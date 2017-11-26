import os
import glob
import re


OutputDataFolder='./output/*'
OutputFiles=list(glob.glob(OutputDataFolder))
FinalOutputFolder='./FinalOutput/'

for fileNumber in range(len(OutputFiles)):
	fileName=OutputFiles[fileNumber].split('_')[1]
	# fileName='661'
	data=""
	print (fileName)
	with open('./DischargeSummary/'+fileName,"r") as myfile:
		data=myfile.read() 
	data = data.lower()
	f1=open('./output/med&gen_'+fileName,"r")
	outputfile=f1.readlines()
	# writer = open(FinalOutputFolder+fileName, 'w') 
	i=0
	for line in outputfile:
		currword=line.split('\t')
		# printte (len(currword))
		# print (currword)
		if len(currword)==6 and (currword[5]!='0\n'):
			word=currword[0]
			wordlen=len(word)
			# print (word)
			st=i
			en=i
			flag=0
			while st+wordlen<len(data):
				if(data[st]==' ' or data[st]=='\t' or data[st]=='\n'):
					st=st+1
				else:
					curr=data[st:st+wordlen]
					curr.lower()
					if(curr==word):
						flag=1
						break
					else:
						st=st+1
				if flag==1:
					break

			en=st+wordlen
			i=en
			DataToBeWritten=fileName+'|'+(str)(st)+'-'+(str)(en)+'|'+word+'|'+currword[5]
			with open(FinalOutputFolder+fileName, 'a') as opfl:
				opfl.write(DataToBeWritten)

	f1.close()
	# i=0
	# prev = 0
	# pres = 0
	# for line in outputfile:
	# 	#..........................real offset
	# 	prev = i
	# 	pres = len(line)

	# 	currword=line.split('\t')
	# 	print(currword)
	# 	if len(currword)==6 and (currword[5]!='0\n'):
	# 		word=currword[0]
	# 		print(word)
	# 		wordlen=len(word)
	# 		flag=0
	# 		while i+wordlen<len(data):
	# 			curr = data[i:i+wordlen]
	# 			print(curr,end=',')
	# 			curr = curr.lower()
	# 			if curr==word :
	# 				if i+wordlen+1<len(data) and data[i+wordlen+1] >='a'
	# 				flag=1
	# 				break
	# 			else:
	# 				i=i+1
	# 		if flag == 1:
	# 			print(i)
	# 			DataToBeWritten=fileName+'|'+(str)(i)+'-'+(str)(i+wordlen)+'|'+word+'|'+currword[5]
	# 			writer.write(DataToBeWritten)
	# 			i+=1
	# 	i = prev+pres
	# 	# if i > 1300 :
	# 	# 	break
	# print('\n')
	# f1.close()

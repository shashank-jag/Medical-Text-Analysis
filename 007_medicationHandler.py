import sys

file = open(sys.argv[1],'r').read()
file = file.lower()

fileName = sys.argv[1].split('/')[-1]

entries = open(sys.argv[2],'r')
entries = entries.readlines()

counter = 0

finalOutput = []

def chk(word,counter):
	if word[0]>='a' and word[0]<='z':
		if file[counter-1] >='a' and file[counter-1]<='z':
			return False
		if file[counter+len(word)] >='a' and file[counter+len(word)]<='z':
			return False

	if word[0]>='0' and word[0]<='9':
		if file[counter-1] >='0' and file[counter-1]<='9':
			return False
		if file[counter+len(word)] >='0' and file[counter+len(word)]<='9':
			return False

	return True



def addPunct(counter):
	#.......................punct.	
	# ind = counter+1
	# while ind<len(file) and (file[ind] == ' ' or file[ind] == '.' or file[ind] == ',' or file[ind] == ';' or file[counter] == '/n'):
	# 	ind+=1
	# 	print(file[ind],'*')
	# if ind != counter:
	# 	ind-=1
	# if ind == counter:
	# 	return counter
	# # print(file[ind],'*')
	# while file[ind] == ' ':
	# 	ind-=1
	# return ind
	if file[counter]=="." or file[counter]==";" :
		counter+=1
	return counter


def addNumber(counter):
	#...................add number
	counter2 = counter
	counter -=1
	# print(counter,len(file),'*')
	while counter > 0 and (file[counter] == ' ' or file[counter] == 'x' or file[counter] == '/n' or (file[counter] >= '0' and file[counter] <= '9' )):
		counter-=1
	if counter != counter2:
		counter+=1
	if counter2 == counter:
		return counter
	while file[counter] == ' ':
		counter+=1
	return counter


for line in entries:
	line = line[:-1]
	pres_entry = line.split('\t')
	if len(pres_entry) < 3:
		continue

	#...........unhandled .............................
	if pres_entry[-1] == '0':
		if pres_entry[0] == "medications" or pres_entry[0] == "medication" or pres_entry[0] == "supplementation" or pres_entry[0] == "morning" or pres_entry[0] == "times" or pres_entry[0] == "day" or pres_entry[0] == "once" or pres_entry[0] == "days" or pres_entry[0] == "minutes" or pres_entry[0] == "a.m." or pres_entry[0] == "p.m." or pres_entry[0] == "once"or pres_entry[0] == "every" :
			pres_entry[-1] = "medication"
		else :
			continue
	word = pres_entry[0]
	
	while  counter + len(word) < len(file) :
	
		if word == file[counter:counter+len(word)].replace("^[0-9a-z]"," ") and chk(word,counter):
			break
		counter+=1
	# print(counter,counter+len(word),file[counter:counter+len(word)])
	strt = counter
	end = counter+len(word)
	# strt=addNumber(counter)
	# end = addPunct(counter+len(word))
	# print(strt,end)
	# print(word)
	insert = [fileName , strt , end , file[strt:end] , pres_entry[-1]]
	# print(insert)
	finalOutput.append(insert)
	counter+=1

for i in range(len(finalOutput)):
	if i < len(finalOutput)-1 and finalOutput[i][1] == finalOutput[i+1][1] :
		continue	
	if 	i < len(finalOutput)-1 and int(finalOutput[i][2]) + 3 >= int(finalOutput[i+1][1]):
		finalOutput[i+1][1] = finalOutput[i][1]
		finalOutput[i+1][3] = finalOutput[i][3] +" "+ finalOutput[i+1][3]
		continue
	if 	i < len(finalOutput)-1 and int(finalOutput[i][2]) >= int(finalOutput[i+1][1]):
		finalOutput[i+1] = [finalOutput[i][0] , finalOutput[i][1],finalOutput[i+1][2],file[int(finalOutput[i][1]):int(finalOutput[i+1][2])],finalOutput[i][-1] if (finalOutput[i][-1] != "0" )  else  finalOutput[i+1][-1]]
		continue

	x = finalOutput[i]	

	fl = True
	for a in x[3]:
		x[3] = x[3].strip()
		if a>="a" and a<="z" :
			fl = False
	if fl:
		continue
	x[3]=x[3].lower()
	if x[3].strip() == "home" or x[3].strip() == "blood" or x[3].strip() == "day" or x[3].strip() == "days." or x[3].strip() == "dep" or x[3].strip() == "days" or x[3].strip() == "every" or len(x[3].strip())<=3 :
		continue
	x = [str(i) for i in x]
	s = x[0]+'|'+x[1]+'-'+x[2]+'|'+x[3]+'|'+x[4]
	print(s)

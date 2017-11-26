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

for line in entries:
	line = line[:-1]
	pres_entry = line.split('\t')
	if len(pres_entry) < 3:
		continue
	if pres_entry[-1] == '0':
		continue
	word = pres_entry[0]
	# print("****************",word,"****************")
	while  counter + len(word) < len(file) :
		# print(file[counter] ,end='')
		if word == file[counter:counter+len(word)].replace("^[0-9a-z]"," ") and chk(word,counter):
			break
		counter+=1
	# print(fileName +'|' + str(counter) +'|' + str(counter+len(word))  +'|' + word  +'|' + pres_entry[-1])
	insert = [fileName , counter,counter+len(word),word,pres_entry[-1]]
	if len(finalOutput) > 0 and finalOutput[-1][-1]==insert[-1]:
		x = finalOutput[-1]
		if insert[1] == x[2]+1:
			insert[3] = x[3]+" "+insert[3]
			insert[1] = x[1]
			finalOutput = finalOutput[:-1]
	finalOutput.append(insert)
	counter+=1
# print(sys.argv[0],sys.argv[1],"done")

for x in finalOutput:
	x = [str(i) for i in x]
	s = x[0]+'|'+x[1]+'-'+x[2]+'|'+x[3]+'|'+x[4]
	print(s)

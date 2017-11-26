import sys

print(sys.argv[1],sys.argv[2])

file = open(sys.argv[1],'r').read()
file = file.lower()


fileName = sys.argv[1].split('/')[-1]


entries = open(sys.argv[2],'r')
entries = entries.readlines()

counter = 0

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
#	print(line)
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
	print(fileName +'|' + str(counter) +'|' + str(counter+len(word))  +'|' + word  +'|' + pres_entry[-1])
	counter+=1
print(sys.argv[0],sys.argv[1],"done")

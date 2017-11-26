import sys

fileRead = open(sys.argv[1],'r').readlines()

entries = []
for line in fileRead :
	entries.append(line.split('\t'))
	print(entries[-1])	


print("done-->1")

realOutput = []
i=0

while i< len(entries) :
	print(i)
	j = i+1
	while j+1 <len(entries) and entries[i][-1] == entries[j][-1] and entries[i][-1][0]!='0':
		entries[i][0] += " " + entries[j][0]
		j+=1
	realOutput.append(entries[i])
	i=j
	print(i)



for x in realOutput:
	print(x)

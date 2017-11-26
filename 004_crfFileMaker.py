import sys
import os

try :
#	os.system("rm -r CombinedModel/*")
#	os.system("rm -r SeperateModel/*")
#	os.mkdir("./CombinedModel")
	os.mkdir("./SeperateModel")
except :
	print("*_*")
finally :
#	os.system("rm -r CombinedModel/*")         
	os.system("rm -r SeperateModel/*")
	print("Resources initialised" )
f = open(sys.argv[1],'r').read()

name = { 0 : "mode" ,1 : "frequency" , 2 : "medication" , 3 : "duration" , 4 : "reason", 5 : "dosage"  }
index = { "mode" : 0 , "frequency" : 1 ,"medication" : 2, "duration" : 3 , "reason" : 4 , "dosage" : 5 ,"0" : -1  }
total = 6


#complete_writer = open("./CombinedModel/train",'w')
partial_writer = []



for i in range(0,total):
	partial_writer.append(open("./SeperateModel/"+name[i],"w+"))
	


f = f.split('\n')

for line in f:
#	line = line[:-1]
	entries = line.split('\t')
	print(entries)
	if len(entries) < 5 :
		break
	typeOfEntry = index[entries[-1] ] 
	if typeOfEntry == -1 :
#		complete_writer.write(line+'\n')
		for files in partial_writer : 
			files.write('\t'.join(entries)+'\n')
#			print(line)
	else :
		print(name[typeOfEntry],typeOfEntry)
		for i in range(0,total) : 
			if i == typeOfEntry :
				print("_",i,entries)
				partial_writer[i].write('\t'.join(entries)+'\n')
			else :
				p = entries[:]
				entries[-1] = "0"
				partial_writer[i].write('\t'.join(entries)+'\n')
				entries = p[:]
for i in range(0,total):
	partial_writer[i].close()

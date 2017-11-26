import sys
#f = open("MedExOutput/11995" , 'r' ).read()
#print(f)
f = open("MedExOutput/"+sys.argv[1] , 'r' ).read()
#print(f)
f=f.split('\n')
#print(f)
clean_label = []
clean_relation = []  
for line in f:
	l = ""
#	print(line)	
#	line = line.replace("|*",'|')
#	print(line)
#	for i in range(len(line)-1,0-1):
#		if l[i] == '|':
#			ct+=1
#		if ct%4 == 0 :
#			clean.append(l)
#			break
#		l = line[i] + l
	i = 0
	while i < len(line) and line[i]>='0' and line[i] <='9':
		i += 1
	i += 1
	while i < len(line) and line[i]!='|' :
		i += 1
	i += 1
	while i < len(line) :
		l += line[i]	
		i += 1
#	print("****************",l)
	if l.count('|') == 3:
		clean_label.append(l)
	else :
		clean_relation.append(l)					
#print(clean_label)
wr1 = open('Clean/medEx_entity_'+sys.argv[1],'w+')
wr2 = open('Clean/medEx_relation_'+sys.argv[1],'w+')

for x in clean_label :
	wr1.write(x+'\n')
for x in clean_relation : 
	wr2.write(x+'\n')

print("******file labels made******")
#print(clean_relation)
#print(clean_label)

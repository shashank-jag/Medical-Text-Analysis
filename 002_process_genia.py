import sys
f = open("Clean/genia_tagged_"+sys.argv[1],'r').read()
f= [l.split('|') for l in f.split()]
#print(f)

entities = {}

for x in f:
	if x[2] in entities.keys() :
		entities[x[2]].append(x)
	else :
		entities[x[2]]=[]
		entities[x[2]].append(x)	
	

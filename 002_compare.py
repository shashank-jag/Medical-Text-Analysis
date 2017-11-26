import sys
dic_gen = {}
dic_med = {}

f = open('Clean/genia_tagged_'+sys.argv[1],'r').read()
f = f.split('\n')
for line in f :
	if len(line) == 0:
		break
#	print(line)
	x = line.split('|')
#	print(x)
	
	dic_gen[x[1] ] = x

f = open('Clean/medEx_entity_'+sys.argv[1],'r').read()
f = f.split('\n')
for line in f :
#	print(line)
	x = line.split('|')
	dic_med[x[0] ] = x[1:]

#print(dic_med)

for x in dic_med.keys():
#	if x in dic_gen.keys() :
#		print(dic_gen[x],'*'*100,dic_med[x])
	words = x.split()
	for y in words :
		if y in dic_gen.keys():
			print(x,'|',y,dic_gen[y],'|',dic_med[x])



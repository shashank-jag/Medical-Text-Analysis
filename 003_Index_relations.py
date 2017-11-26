# Trying to figure out if there are any relation between various entity types and the genia tags associated with those entities.
# Maintaining count of various relations ancountered and their frequencies. 

import os
import HelperFunctions as parser 


attribute_types= {}

for filename in os.listdir(os.getcwd()+"/Analysis"):
	#print(os.getcwd()+"/Analysis/"+filename)
	#path = "Analysis/"+str(filename)
	f = open(str("Analysis/"+str(filename)),'r').read()
	#f = open(path,'r')
	#print(f)
	doc = []
	f = f.split('\n')
	for line in f :
		try :
			tag = parser.geniaVsmedEx_reader(line)
	#		print(tag)
			doc.append(tag)
		except :
			#print("Done converting  this back----*_*")
			#print(line) 
			continue
	#for i in range(0,len(doc)):
	i = 0
	while i < len(doc):
		attribute = doc[i]["medEx"][0]
		relation = [ doc[i]["genia"][1] ]
		if i+1 < len(doc):
			while i<len(doc)-1 and doc[i+1]["name"] == doc[i]["name"]:
				i+=1
				relation.append(doc[i]["genia"][1])
			if len(relation)>1 :
				i -= 1
		i += 1
		relation = tuple(relation)
		#print(attribute,relation)
		if attribute in attribute_types.keys() :
			if relation in attribute_types[attribute].keys():
				attribute_types[attribute][relation]+=1
			else :
				attribute_types[attribute][relation]=1	
		else :
			attribute_types[attribute]={}
			attribute_types[attribute][relation]=1 
#print(attribute_types)

rules = { x:[] for x in attribute_types.keys() }
for attribute in attribute_types.keys():
	for relation in attribute_types[attribute].keys():
		l=[]
		l.append(attribute_types[attribute][relation])
		l.append(relation)
		rules[attribute].append(l)
	rules[attribute].sort(reverse=True)
#print(rules)

res = open("Rules_adjustment",'w')
for key in rules.keys():
	res.write(str(key)+'\n')
	for lis in rules[key]:
		for i in lis:
			res.write(str(i)+'\t')
		res.write('\n')
	res.write('\n'+'*'*100+'\n'*2)
res.close()
	

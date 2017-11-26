def geniaVsmedEx_reader(s):
	x = s.split('|')
	ret = {}
	ret['name'] = x[0].strip()
	
	#temp 
	temp = x[1].replace('[','')
	temp = temp.replace(']','')
	temp = temp.replace(',','')
	temp = temp.replace('  ',' ')
	temp = temp.replace('\'','')
	temp = temp.split()
	temp = temp[1:]
	ret['genia'] = temp
	
	#medEx 
	temp = x[2].replace('[','')
	temp = temp.replace(']','')
	temp = temp.replace(',','')
	temp = temp.replace('  ',' ')
	temp = temp.replace('\'','')
	temp = temp.split()
	#temp = temp[1:]
	ret['medEx'] = temp

	return ret

#test........
#print("nexium | nexium ['nexium', 'NN', 'I-NP', 'O'] | ['DBN', '6440', '6446']")

#x = geniaVsmedEx_reader("nexium | nexium ['nexium', 'NN', 'I-NP', 'O'] | ['DBN', '6440', '6446']")
#print(x)

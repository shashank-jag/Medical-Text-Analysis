import subprocess
import os.path
import fcntl

data = ["this is just mad"] 

path_to_genia = "/home/guestdsac/qwerty/shashank/geniatagger-3.0.2"

os.chdir(path_to_genia)

#dir_to_tagger = os.path.dirname(path_to_genia)

#tagger = subprocess.call("ls",shell=True)
tagger = subprocess.Popen("./geniatagger",stdin=subprocess.PIPE, stdout=subprocess.PIPE)
#print(tagger)

results = []
print("*********")
for oneline in data:
	tagger.stdin.write((oneline+'\n').encode('utf-8'))
	tagger.stdin.flush()
	#print('0')
	print(oneline)
	while (True):
		try :
			r = tagger.stdout.readline()[:-1]
		except : 
			continue
		r=str(r)
		print(r.split('\\t'))
		results.append(r.split('\\t'))
		break
print(results)
print("Im mad")

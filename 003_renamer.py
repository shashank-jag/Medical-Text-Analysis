import sys 

f = open(sys.argv[1],"r").read()

wr = open(sys.argv[1].split('_')[-1],"w+")
print(f)
wr.write(f)
wr.close()
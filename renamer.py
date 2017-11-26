import sys 
f = open(sys.argv[0],"r").read()

wr = open(sys.argv[0].split('_')[-1],"w+")
print(f)
wr.write(f)
wr.close()
import numpy
from sklearn.decomposition import PCA

data = open("data",'r').read();   #...read as numpy arrays
total_components = 1000 #....get rows here

pca = PCA(n_components= (int) total_components * (0.5) ) #...change values for experintation -> reduce dimention by different ratios...

pca.fit(data)  #...pca trained

#...print cintribution of the various eigen values to our pca
print pca.explained_varience_ratio_

first_pc = pca.component[0]
second_pc = pca.component[1]

transformed_data = pca.transform(data)

#...write transformed data .....alter accordingly
wri = open("data2","w")
for i in transformed_data:
	wri.write(i+'\n')

wri.close()

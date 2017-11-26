mkdir SeperateModelsOutput

#cd CRF++0.58
#ls

#head -n 10 Medication.txt

for entry in "./Models"/*
do
	entry=`basename "$entry"`
#	echo "./Models/"$entry   ./CRF++-0.58/crf_learn Medication.txt "./Models/"$entry 
	./CRF++-0.58/crf_test -m "./Models/"$entry  testfile.txt >> ./SeperateModelsOutput/$entry 
done

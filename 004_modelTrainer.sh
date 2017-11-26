mkdir Models
#cd CRF++0.58
#ls

#head -n 10 Medication.txt

for entry in "./SeperateModel"/*
do
	entry=`basename "$entry"`
#	echo "./Models/"$entry   ./CRF++-0.58/crf_learn Medication.txt "./Models/"$entry 
	./CRF++-0.58/crf_learn -a CRF-L2 ./Medication.txt "./SeperateModel/"$entry  "./Models/"$entry & 
done

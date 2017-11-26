#--> INPUT bash 004_multipleFileRunner.sh Models input output

#........argv1 - model path with name
#........argv2 - inputfile path
#........argv3 - output path

#........file paths without /

# Change CRF++ path accordingly


while [[ $# -lt 3 ]]
do
	echo "3 arguments required........see decription "
done


modelPath=$1
files=$2
outputPath=$3

mkdir $outputPath


for models in $modelPath/* 
do
mkdir "./"$outputPath"/"`basename "$models"`

for entry in $files/* 
do
#	echo $entry  
	entry=`basename "$entry"`
	echo $entry "./"$models "./"$files"/"$entry  "./"$outputPath"/"`basename "$models"`"/"$entry

#       echo "./Models/"$entry   ./CRF++-0.58/crf_learn Medication.txt "./Models/"$entry 
	./CRF++-0.58/crf_test -m "./"$models  "./"$files"/"$entry > "./"$outputPath"/"`basename "$models"`"/"$entry  &
done
done

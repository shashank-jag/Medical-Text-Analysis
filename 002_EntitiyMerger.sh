mkdir tempFolder
pathToDischarge=$2
for file in $1/* :
do
	echo $file
	rm temp
	# time python3 001_spanMatcherPro.py $pathToDischarge/`basename $file` $file 
	time python3 001_spanMatcherPro.py $pathToDischarge/`basename $file` $file >> temp
	# cat temp > ./tempFolder/`basename $file`
	rm $file
	cat temp >> $file
	# break
done
echo "Doneeeeeeeeeeeeeeeeeeeeee"

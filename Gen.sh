mkdir tempFolder
pathToDischarge=$2
type_=$3
mkdir ./tempFolder/dosage
mkdir ./tempFolder/duration
mkdir ./tempFolder/frequency
mkdir ./tempFolder/mode
mkdir ./tempFolder/reason
mkdir ./tempFolder/medication

for file in $1/* :
do
	echo $file
	rm temp
	
	if [ $type_ -eq 1 ]
	then
		time python3 001_dosageHandler.py $pathToDischarge/`basename $file` $file > temp
		cat temp > ./tempFolder/dosage/`basename $file`

		echo "dosage " `basename $file` "made"
	fi
	if [ $type_ -eq 2 ]
	then
		time python3 005_reasonHandler.py $pathToDischarge/`basename $file` $file > temp
		cat temp
		echo "***********************************"
		cat temp > ./tempFolder/reason/`basename $file`

		echo "reason " `basename $file` "made"
	fi
	if [ $type_ -eq 3 ]
	then
		time python3 002_durationHandler.py $pathToDischarge/`basename $file` $file > temp
		# cat temp
		echo "***********************************"
		cat temp > ./tempFolder/duration/`basename $file`

		echo "duration" `basename $file` "made"
	fi

	if [ $type_ -eq 4 ]
	then
		time python3 003_frequencyHandler.py $pathToDischarge/`basename $file` $file > temp
		# cat temp
		echo "***********************************"
		cat temp > ./tempFolder/frequency/`basename $file`

		echo "frequency " `basename $file` "made"
	fi

	if [ $type_ -eq 5 ]
	then
		time python3 004_modeHandler.py $pathToDischarge/`basename $file` $file > temp
		# cat temp
		echo "***********************************"
		cat temp > ./tempFolder/mode/`basename $file`

		echo "mode " `basename $file` "made"
	fi

	if [ $type_ -eq 6 ]
	then
		time python3 007_medicationHandler.py $pathToDischarge/`basename $file` $file > temp
		# cat temp
		echo "***********************************"
		cat temp > ./tempFolder/medication/`basename $file`

		echo "medication " `basename $file` "made"
	fi

	# time python3 002_durationHandler.py $pathToDischarge/`basename $file` $file > temp
	# cat temp > ./tempFolder/duration/`basename $file`
	
	# echo "duration " `basename $file` "made"

	# time python3 003_frequencyHandler.py $pathToDischarge/`basename $file` $file > temp
	# cat temp > ./tempFolder/frequency/`basename $file`
	
	# echo "frequency " `basename $file` "made"


	# cat temp > ./tempFolder/`basename $file`
	# rm $file
	# cat temp >> $file
	# break
done
echo "Doneeeeeeeeeeeeeeeeeeeeee"

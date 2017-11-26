
for file in ./output/* ;
do
	D2=$(dirname $file)
	DIRNAME2=$(basename $file)
	echo $file `dirname "$file"` $DIRNAME2

	# java -jar compare_annotator.jar ./Annotation ./tempFolder ./DischargeSummary ./log_shashank dosage


	java -jar compare_annotator.jar ./Annotation $file ./DischargeSummary ./log_shashank_$DIRNAME2 $DIRNAME2 > temp_$DIRNAME2  &
	echo temp_$DIRNAME2
	echo ./Annotation $file ./DischargeSummary /log_shashank_$DIRNAME2 $DIRNAME2
	echo "*************************************************************************"
done
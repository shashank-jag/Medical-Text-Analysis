for file in ./* :
do
	echo $file
	python3 003_renamer.py $file
done
rm med*
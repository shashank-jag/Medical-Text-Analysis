mkdir temp
for file in $1/* :
do
	echo $file
	rm temp
	time python 004_single_Entity.py $file > temp
	cat temp > ./temp/$file
done
echo "Doneeeeeeeeeeeeeeeeeeeeee"

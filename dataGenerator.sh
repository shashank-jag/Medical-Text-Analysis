#!/bin/bash
#This script prepares data from MedEx outputs as well as Gena tagged outputs on the same dataset.
#This data can the be used to derieve several rules or patterns between the pos tag sequence and possible medical term that can go with various those sequences.


mkdir Clean
mkdir Analysis

i=0
limit=1000
for entry in "DischargeSummary"/*
do
	entry=`basename "$entry"`
	dest="Clean/genia_tagged_""$entry"
	echo "$dest"
	python 002_genia.py "$entry" > "$dest"
#	python 002_process_genia.py "$entry"
	python 002_medEx_builder.py "$entry"
	i=$((i + 1))
	analiti="Analysis/geniaVSmedEx_""$entry"
	python 002_compare.py "$entry" > "$analiti" 
#	python 002_compare.py "$entry"
	echo $i
	if [ $i -eq $limit ];
	then
		echo "Done parsing" $i $limit 
		break
	fi
#	break
done

python 003_Index_relations.py

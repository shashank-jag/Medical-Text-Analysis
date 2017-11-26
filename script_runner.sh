mkdir Clean

python 002_genia.py 661 > Clean/genia_tagged_661
python 002_process_genia.py 661
python 002_medEx_builder.py 661


mkdir Analysis

python 002_compare.py 661 > Analysis/geniaVSmedEx_661

echo 'Date prepared for CRF training'


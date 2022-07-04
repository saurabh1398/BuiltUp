#!/usr/bin/bash
cwd=$PWD
filename=$1
filename="$cwd""/data/District_Names/""$filename"
n=1
while read line; do
dist="${line// /}" 
dist1=$dist
dist="Landsat7_"$dist
dist="$cwd""/data/IndiaSat/"$dist"/Villages"
echo "Processing district $dist"
count=0
for file in $dist/*
do
	count=$((count+1))
	echo "Village No: $count"
	file2="${file// /}"
	file3="${file##*/}"
	file3="$dist1""/""$file3"

	echo "Processing Village: $file2"
	python3 "$cwd""/src/LC_classification/final_classification_processing.py" $file2 $file3
done
echo "Number of Villages processed in $dist1"
echo "$count"
n=$((n+1))

done < "$filename"
echo "$n"
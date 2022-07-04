#!/usr/bin/bash
cwd=$PWD
statename=$1
statename=${statename// /_}
echo "${statename// /_}"
filename=$2
filename="$cwd""/data/District_Names/""$filename"
echo "$filename"
n=1
while read line; do
dist=$line
dist="${line// /}"
fname="$cwd""/data/IndiaSat/Results/"$dist
echo "Processing District: $dist"
count=0
for file in $fname/*
do
	count=`expr $count + 1`
	file2="${file// /}"
	echo "Processing Village: ${file2##*/}"
	python3 "$cwd""/src/vill1.py" $statename $dist ${file2##*/}
done
echo "Number of Villages processed in $dist"
echo "$count"
n=$((n+1))
done < $filename
echo "$n"

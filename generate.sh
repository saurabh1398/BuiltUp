#!/usr/bin/bash
cwd=$PWD
statename=$1
echo "${statename// /_}"
stateshapefile=$2
filename=$3
filename="$cwd""/data/District_Names/""$filename"
scriptpath="$cwd""/src/Getting_villages_in_dist.py"
echo $filename
echo "$stateshapefile"
n=1
while read line; do
python3 "$scriptpath" "${line// /_}" "$statename" "$stateshapefile"	
n=$((n+1))
done < "$filename"
echo "$n"
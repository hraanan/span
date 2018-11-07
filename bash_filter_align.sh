#!/bin/bash


fPath=$SPAN/
pyFuncFile=$fPath"filter_ADE.py"
IN_FILE_NAME=$1
#OUT_FILE_NAME=$2
CORES=$2

# Work out lines per file.

total_lines=$(wc -l <${IN_FILE_NAME})
((lines_per_file = (total_lines + CORES - 1) / CORES))

# Split the actual file, maintaining lines.

split --lines=${lines_per_file} ${IN_FILE_NAME} in_temp_file.

# Debug information

echo "Total lines     = ${total_lines}"
echo "Lines  per file = ${lines_per_file}"    

wait
count=0
for f in in_temp_file.*;
do 
	python3 $pyFuncFile $f &
	
done

wait
echo "All processes done!"
cat in_temp_file.??_ADE.txt > temp_ADE_all.txt
cat in_temp_file.??_NO_ADE.txt > temp_NO_ADE_all.txt
echo "combine files!"
wait
echo 'Sourec\tTarget\tSl\tTl\tLigand\tRMSD\tAlign CA\tRaw alignment score\tAligned Residues\tLigand center distance\tStructural Distance\n' | cat - temp_ADE_all.txt > align_filter_ADE_all.txt
wait
echo 'Sourec\tTarget\tSl\tTl\tLigand\tRMSD\tAlign CA\tRaw alignment score\tAligned Residues\tLigand center distance\tStructural Distance\n' | cat - temp_NO_ADE_all.txt > align_filter_NO_ADE_all.txt
wait
wait
rm in_temp_file.* temp_ADE_all.txt temp_NO_ADE_all.txt

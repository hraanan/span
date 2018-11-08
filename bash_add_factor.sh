#!/bin/bash


fPath=$SPAN/
pyFuncFile=$fPath"add_factor.py"
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
cat in_temp_file.??_out.txt > temp_all.txt
echo "combine files!"
wait
echo='Source\tTarget\tsource cof\tTarget cof\tQl\tTl\tLigand\tEC distance\tRMSD\tAlign CA\tRaw alignment score\tAligned Residues\tLigand center distance\tStructural Distance\tNormalized RMSD\tNormalized CA\tNormalizesd metal distance\tNormalized stractural distance\tFactor\n' | cat - temp_all.txt > align_filter_NO_ADE_all_with_factor.txt
wait
rm in_temp_file.* 

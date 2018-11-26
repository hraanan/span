#!/bin/bash

#SBATCH --partition=main          # Partition (job queue)
#SBATCH --job-name=OMP            # Assign an 8-character name to your job
#SBATCH --nodes=1                 # Number of nodes
#SBATCH --ntasks=1                # Number of tasks (usually = cores) on each node
#SBATCH --cpus-per-task=1         # Threads per process (or per core)
#SBATCH --mem=1000                # Real memory required (MB)
#SBATCH --time=00:01:00           # Total run time limit (HH:MM:SS)
#SBATCH --output=slurm.%N.%j.out  # STDOUT output file
#SBATCH --error=slurm.%N.%j.out   # STDERR output file
#SBATCH --export=ALL              # Export you current env to the job env


export LD_LIBRARY_PATH=/home/hr253/pymol:$LD_LIBRARY_PATH
IN_FILE_NAME=$1
CORES=$2
# Work out lines per file.
total_lines=$(wc -l <${IN_FILE_NAME})
((lines_per_file = (total_lines + CORES - 1) / CORES))
# Split the actual file, maintaining lines.
split --lines=${lines_per_file} ${IN_FILE_NAME} align_temp.
# Debug information
echo "Total lines     = ${total_lines}"
echo "Lines  per file = ${lines_per_file}"    
wait
count=0
mkdir cnt
mkdir err
mkdir out
mkdir run
for f in align_temp.*;
do 
	sbatch test_run $f
done
wait
echo "All processes done!"
echo "combine files!"
#cat align_temp.*_out.txt > temp_all.txt
#echo 'Sourec\tTarget\tSl\tTl\tLigand\tRMSD\tAlign CA\tRaw alignment score\tAligned Residues\tLigand center distance\tStructural Distance\n' | cat - temp_all.txt > temp && mv temp align_out_all.txt


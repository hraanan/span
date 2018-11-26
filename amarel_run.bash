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

#export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
#alias python=/home/hr253/pymol/bin/python2.7
export LD_LIBRARY_PATH=/home/hr253/pymol:$LD_LIBRARY_PATH

IN_FILE_NAME=$1
PYTHON_FILE=$2

/home/hr253/pymol/bin/python ~/span/$PYTHON_FILE $IN_FILE_NAME




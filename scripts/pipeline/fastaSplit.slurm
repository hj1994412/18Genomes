#!/bin/bash

#fastaSplit.slurm basically from quick-start guide

#SBATCH -n 1 # Number of cores requested                                                        #Not Sure
#SBATCH -N 1 # Ensure that all cores are on one machine                         #Not Sure
#SBATCH -t 04:00:00 # Runtime
#SBATCH -p serial_requeue # Partition to submit to
#SBATCH --mem=1000 # Memory per cpu in MB (see also --mem-per-cpu)	#Not Sure
#SBATCH -o fastaSplit${1}.out # Standard out goes to this file
#SBATCH -e fastaSplit${1}.err # Standard err goes to this filehostname

#Prepare reference sequence for alignment
fasta-splitter.pl --n-parts=1 --line-length=60 $1

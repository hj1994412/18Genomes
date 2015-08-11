#!/bin/bash

#genomeBuild_last.slurm basically from quick-start guide

#SBATCH -n 1 # Number of cores requested							#Not Sure
#SBATCH -N 1 # Ensure that all cores are on one machine				#Not Sure
#SBATCH -t 0-2:00 # Runtime 									
#SBATCH -p serial_requeue # Partition to submit to					
#SBATCH --mem=4000 # Memory per cpu in MB (see also --mem-per-cpu)	#Not Sure
#SBATCH -o genomeBuild.out # Standard out goes to this file
#SBATCH -e genomeBuild.err # Standard err goes to this filehostname

#Prepare reference sequence for alignment
lastdb -cR01 hmeldb $GENOMES/data/reference/Hmel2.fa


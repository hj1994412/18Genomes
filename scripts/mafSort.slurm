#!/bin/bash
#
# mafSort.slurm from tophat_manyfiles.sbatch example
#
#SBATCH -p serial_requeue # Partition
#SBATCH -n 1              # one core
#SBATCH -N 1              # on one node
#SBATCH -t 0-12:00         # Running time of 12 hours
#SBATCH --mem 1000        # Memory request of 1 GB
#SBATCH -o mafSort.out # Standard output
#SBATCH -e mafSort.err # Standard error


$GENOMES/scripts/maf-sort.sh $1 


#!/bin/bash

#alignScores.slurm  

#SBATCH -n 1
#SBATCH -t 0-1:00
#SBATCH --mem=500
#SBATCH -p serial_requeue
#SBATCH -o %j.out
#SBATCH -e %j.err

grep flattened $1 | awk '{print $2}' | uniq > $GENOMES/tmp.txt

alignScores.py $GENOMES/tmp.txt $1

rm $GENOMES/tmp.txt

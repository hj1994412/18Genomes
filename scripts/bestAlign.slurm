#!/bin/bash

#alignScores.slurm  

#SBATCH -n 1
#SBATCH -t 10:00:00
#SBATCH --mem=10000
#SBATCH -p serial_requeue
#SBATCH -o redo%j.out
#SBATCH -e redo%j.err

base=$(basename $1 _alns.maf)

grep flattened $1 | awk '{print $2}' | sort -u  > $GENOMES/$1tmp.txt

bestAlignment.py $GENOMES/$1tmp.txt $1 $base\_bestAlign.maf

rm $GENOMES/$1tmp.txt

#!/bin/bash

#alignScores.slurm  

#SBATCH -N 1
#SBATCH -n 1
#SBATCH -t 0-1:00
#SBATCH --mem=50000
#SBATCH -p serial_requeue
#SBATCH -o alignScores.out
#SBATCH -e alignScores.err

alignScores.py $1


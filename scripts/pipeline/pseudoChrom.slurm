#!/bin/bash

#SBATCH -p serial_requeue
#SBATCH -n 1
#SBATCH -N 1
#SBATCH --mem=5000
#SBATCH -t 0-05:00
#SBATCH -e pseudoChrom.err
#SBATCH -o pseudoChrom.out

pseudoChrom.py $1 $2

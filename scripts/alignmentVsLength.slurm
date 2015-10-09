#!/bin/bash

#alignmentVsLength.slurm
#send alignmentVsLength.py to slurm

#SBATCH -p serial_requeue
#SBATCH --mem=5000
#SBATCH -t 0-5:00
#SBATCH -n 1
#SBATCH -N 1
#SBATCH -o aVl.out
#SBATCH -e aVl.err

alignmentVsLength.py $1 $2 "alignVsLength_Hmel"

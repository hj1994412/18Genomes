#!/bin/bash

#SBATCH -p serial_requeue
#SBATCH -n 1
#SBATCH -N 1
#SBATCH -t 0-0:20
#SBATCH --mem=500
#SBATCH -e bestAlignsToBed.err
#SBATCH -o bestAlignsToBed.out


bestAlignsToBed.py $1 $2 $3

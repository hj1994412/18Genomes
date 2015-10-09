#!/bin/bash

#SBATCH -p serial_requeue
#SBATCH --mem=50000
#SBATCH -n 1
#SBATCH -N 1
#SBATCH -o noOverlaps.out
#SBATCH -e noOverlaps.err
#SBATCH -t 300

noOverlap.py $1

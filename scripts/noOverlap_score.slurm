#!/bin/bash

#SBATCH -p serial_requeue
#SBATCH --mem=50000
#SBATCH -n 1
#SBATCH -N 1
#SBATCH -o noOverlap_score.out
#SBATCH -e noOverlap_score.err
#SBATCH -t 300

noOverlap_score.py $1

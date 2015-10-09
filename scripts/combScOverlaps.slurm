#!/bin/bash

#SBATCH -p serial_requeue
#SBATCH -N 1
#SBATCH -n 1
#SBATCH --mem=200
#SBATCH -t 0-10:00
#SBATCH -o %j\_noScO.out
#SBATCH -e %j\_noScO.err

cat *ScOverlap.maf | maf-sort.sh > allScOverlaps.maf

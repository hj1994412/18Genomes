#!/bin/bash

#concatenateMaf.slurm

#SBATCH -n 1
#SBATCH -t 12:00:00
#SBATCH -p serial_requeue
#SBATCH --mem=1000
#SBATCH -o concatMaf.out
#SBATCH -e concatMaf.err

cat *.maf > concatMafM100.maf

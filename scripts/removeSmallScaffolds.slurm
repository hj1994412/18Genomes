#!/bin/bash

#removeSmallScaffolds.slurm
#sends a fasta file, along with a base name and cutoff, to removeSmallScaffolds.py

#SBATCH -n 1
#SBATCH -t 0-1:00
#SBATCH --mem=500
#SBATCH -p serial_requeue
#SBATCH -o clipper%j.out
#SBATCH -e clipper%j.err

removeSmallScaffolds.py $1 $(basename $1 .fasta) $2

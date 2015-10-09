#!/bin/bash

#SBATCH -p serial_requeue
#SBATCH -n 1
#SBATCH -N 1
#SBATCH -t 0-01:00
#SBATCH --mem=5000
#SBATCH -o repeatMask.out
#SBATCH -e repeatMask.err

RepeatMasker --species "heliconius melpomene" $GENOMES/data/reference/Hmel2_chromosomes.fa

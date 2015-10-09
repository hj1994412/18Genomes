#!/bin/bash

#scafToChrom.slurm  
#convert the Hmel2 genome fasta file to be sorted by chromosomes

#SBATCH -n 1
#SBATCH -t 0-1:00
#SBATCH --mem=1000
#SBATCH -p serial_requeue
#SBATCH -o scafToChrom.out
#SBATCH -e scafToChrom.err

scaffToChrom.py

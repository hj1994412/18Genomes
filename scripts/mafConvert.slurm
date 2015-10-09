#!/bin/bash

#mafConvert.slurm

#take a maf file and convert it to a BAM file

#SBATCH -p serial_requeue
#SBATCH -n 1
#SBATCH -N 1
#SBATCH --mem=500
#SBATCH -o mafToSam_%j.out
#SBATCH	-e mafToSam_%j.err
#SBATCH -t 0-05:00

maf-convert.py sam $1 > $1.sam 

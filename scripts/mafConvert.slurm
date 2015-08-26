#!/bin/bash

#mafConvert.slurm

#take a maf file and convert it to a BAM file

#SBATCH -p serial_requeue
#SBATCH -n 1
#SBATCH -N 1
#SBATCH --mem=500
#SBATCH -o mafToSam_%j.out
#SBATCH	-e mafToSam_%j.err

maf-convert.py sam maf/$1 > sam/$2.sam | samtools view -bt $GENOMES/data/reference/Hmel2.fa.fai - > bam/$2.bam 

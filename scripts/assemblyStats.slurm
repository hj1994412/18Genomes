#!/bin/bash

#assemblyStats.slurm
#submits a batch job to do assemblyStats.py, which outputs 2 csv files - one that has a distribution of scafffold sizes and one that is an inverse density of those sizes

#SBATCH -n 1
#SBATCH -t 0-1:00
#SBATCH --mem=500
#SBATCH -p serial_requeue
#SBATCH -o Stats_%j.out
#SBATCH -e Stats_%j.err

assemblyStats.py $1 $(basename $1 _copy.fasta)

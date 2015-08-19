#!/bin/bash

#generalSlurm.slurm  
#Hopefully, will be able to submi short scripts as slurm jobs without having to make individual files

#SBATCH -n 1
#SBATCH -t 0-1:00
#SBATCH --mem=500
#SBATCH -p serial_requeue
#SBATCH -o $2.out
#SBATCH -e $2.err

$1

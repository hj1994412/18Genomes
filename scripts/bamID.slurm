#!/bin/bash
#SBATCH -n 1 # Number of cores requested
#SBATCH -N 1 # Ensure that all cores are on one machine
#SBATCH -t 5 # Runtime in minutes
#SBATCH -p serial_requeue # Partition to submit to
#SBATCH --mem=100 # Memory per cpu in MB (see also --mem-per-cpu)
#SBATCH -o hostname.out # Standard out goes to this file
#SBATCH -e hostname.err # Standard err goes to this filehostname

samtools view -H @ARGV
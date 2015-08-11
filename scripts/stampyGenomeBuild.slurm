#!/bin/bash

##Attempted script for initial genome analysis##
##8/4/15##


#SBATCH -n 1 # Number of cores requested
#SBATCH -N 1 # Ensure that all cores are on one machine
#SBATCH -t 100 # Runtime in minutes									#Unsure
#SBATCH -p serial_requeue # Partition to submit to					#Unsure
#SBATCH --mem=3000 # Memory per cpu in MB (see also --mem-per-cpu) 	#Unsure
#SBATCH -o genome.out # Standard out goes to this file
#SBATCH -e genome.err # Standard err goes to this filehostname

./stampy.py -G Hmel2 Hmel2_2015-07-17/Hmel2.fa		#Builds Genome File

./stampy.py -g Hmel2 -H Hmel2						#Builds Hash File in ~10 min





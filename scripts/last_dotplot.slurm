#!/bin/bash
#last_dotplot.slurm basically from quick-start guide

#SBATCH -n 1 # Number of cores requested                        #Not Sure
#SBATCH -t 01:00:00 # Runtime                                                           
#SBATCH -p serial_requeue # Partition to submit to                                      
#SBATCH --mem=1000 # Memory per cpu in MB (see also --mem-per-cpu)      #Not Sure
#SBATCH -o last_dotplot.out # Standard out goes to this file
#SBATCH -e last_dotplot.err # Standard err goes to this filehostname

#Prepare reference sequence for alignment
python $GENOMES/scripts/last-dotplot.py ./*.maf alignment.png

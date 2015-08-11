#!/bin/bash
#
# genomeAlign_last.sbatch from tophat_manyfiles.sbatch example
#
#SBATCH -J lastal         # A single job name for the array
#SBATCH -p serial_requeue # Partition
#SBATCH -n 1              # one core
#SBATCH -N 1              # on one node
#SBATCH -t 0-2:00         # Running time of 2 hours
#SBATCH --mem 4000        # Memory request of 4 GB
#SBATCH -o lastal%A_%a.out # Standard output
#SBATCH -e lastal%A_%a.err # Standard error
 
mkdir trans${SLURM_ARRAY_TASK_ID}_out
cd trans${SLURM_ARRAY_TASK_ID}_out

#find local alignments between query sequences and reference sequences
lastal hmeldb $GENOMES/data/alignments_fasta/SPLITDIR/trans${SLURM_ARRAY_TASK_ID}.fasta \
	> trans${SLURM_ARRAY_TASK_ID}_alns.maf #Do I need this? Should I change the -o 
											#extension to .maf?

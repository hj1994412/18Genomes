#!/bin/bash
#
# genomeAlign_last.sh from tophat.sh example
#
#SBATCH -J lastal         # A single job name for the array
#SBATCH -p serial_requeue # Partition
#SBATCH -n 1              # one core
#SBATCH -N 1              # on one node
#SBATCH -t 24:00:00         # Running time of 24 hours
#SBATCH --mem 2000        # Memory request of 2 GB
#SBATCH -o lastal%A_%a.out # Standard output
#SBATCH -e lastal%A_%a.err # Standard error

#find local alignments between query sequences and reference sequences
lastal -m 1000 $GENOMES/results/hmeldb $GENOMES/data/alignments_fasta/h_melpomene/parts/h_melpomene.part-${SLURM_ARRAY_TASK_ID}.fasta | $GENOMES/scripts/maf-sort.sh > h_melpomene.part-${SLURM_ARRAY_TASK_ID}_alns.maf 

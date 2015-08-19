#!/bin/bash
#
# genomeAlign_last.sbatch from tophat_manyfiles.sbatch example
#
#SBATCH -p serial_requeue # Partition
#SBATCH -n 1              # one core
#SBATCH -N 1              # on one node
#SBATCH -t 0-2:00         # Running time of 2 hours
#SBATCH --mem 10000        # Memory request of 10 GB
#SBATCH -o lastal_m100.out # Standard output
#SBATCH -e lastal_m100.err # Standard error

#find local alignments between query sequences and reference sequences
lastal -m 1000 $GENOMES/results/hmeldb $GENOMES/data/alignments_fasta/h_melpomene/parts/h_melpomene.part-001.fasta  > h_melpomene_part001_m1000_alns.maf

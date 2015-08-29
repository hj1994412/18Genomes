#!/bin/bash
#
# genomeAlign_last.sbatch from tophat_manyfiles.sbatch example
#
#SBATCH -p serial_requeue # Partition
#SBATCH -n 1              # one core
#SBATCH -N 1              # on one node
#SBATCH -t 0-2:00         # Running time of 2 hours
#SBATCH --mem 10000        # Memory request of 10 GB
#SBATCH -o lastal_failedredo_%j.out # Standard output
#SBATCH -e lastal_failedredo_%j.err # Standard error

#find local alignments between query sequences and reference sequences
lastal -m 100 -e 45 -d 45  $GENOMES/results/hmeldb $GENOMES/data/alignments_fasta/h_melpomene/parts/h_melpomene.part-$1.fasta \
> h_melpomene_part-$1_alns_ed45.maf

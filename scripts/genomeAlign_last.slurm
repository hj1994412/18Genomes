#!/bin/bash
#
# genomeAlign_last.sbatch from tophat_manyfiles.sbatch example
#
#SBATCH -p serial_requeue # Partition
#SBATCH -n 1              # one core
#SBATCH -N 1              # on one node
#SBATCH -t 0-24:00         # Running time of 2 hours
#SBATCH --mem 10000        # Memory request of 10 GB
#SBATCH -o lastalR01C3f0m100.out # Standard output
#SBATCH -e lastalR01C3f0m100.err # Standard error

#find local alignments between query sequences and reference sequences
lastal -R 01 -m 100 -C 3 -f 0 $GENOMES/results/hmeldb $1 \
| maf-sort.sh >  $1\_R01C3f0m100_alns.maf

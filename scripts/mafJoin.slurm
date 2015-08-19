#!/bin/bash
#
# mafJoin.slurm from tophat_manyfiles.sbatch example
#
#SBATCH -p serial_requeue # Partition
#SBATCH -n 1              # one core
#SBATCH -N 1              # on one node
#SBATCH -t 0-12:00         # Running time of 12 hours
#SBATCH --mem 5000        # Memory request of 1 GB
#SBATCH -o joinTest.out # Standard output
#SBATCH -e joinTest.err # Standard error

$GENOMES/scripts/maf-join.py h_melpomene.part-484_alns.maf h_melpomene.part-485_alns.maf h_melpomene.part-486_alns.maf > joinTest.maf

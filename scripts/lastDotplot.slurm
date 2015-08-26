#!/bin/bash
#
# lastDotplot.slurm from tophat_manyfiles.sbatch example
#
#SBATCH -p serial_requeue # Partition
#SBATCH -n 1              # one core
#SBATCH -N 1              # on one node
#SBATCH -t 0-12:00         # Running time of 2 hours
#SBATCH --mem 50000        # Memory request of 30 GB
#SBATCH -o lastDotplot.out # Standard output
#SBATCH -e lastDotplot.err # Standard error

$GENOMES/scripts/last-dotplot.py $1 $1_dotplot.png

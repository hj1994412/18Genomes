#!/bin/bash

#SBATCH -J True_Alignments
#SBATCH -p serial_requeue
#SBATCH -n 1
#SBATCH -N 1
#SBATCH -t 0-01:00
#SBATCH --mem=10000
#SBATCH -o mafToBedArray_%A_%a.out
#SBATCH -e mafToBedArray_%A_%a.err

mafToBed.py $GENOMES/results/lastAlignments/chromPipe/h_melpomene.part-"${SLURM_ARRAY_TASK_ID}"_alns.maf $GENOMES/data/alignments_fasta/h_melpomene/h_melpomene_copy.fasta



#!/bin/bash

#bestAlign.slurm

#SBATCH -J bestAlign
#SBATCH -n 1
#SBATCH -t 00:10:00
#SBATCH --mem=100
#SBATCH -p serial_requeue
#SBATCH -o bestAlign%A_%a.out
#SBATCH -e bestAlign%A_%a.err


#find the single best (longest) LAST alignment for each DISCOVAR contig

#assumes the alignment files are in the form <sample>.part-<number>_alns.maf

sample=$1

bestAlignment.py $sample.part-${SLURM_ARRAY_TASK_ID}_alns.maf $sample.part-${SLURM_ARRAY_TASK_ID}_bestAlign.maf

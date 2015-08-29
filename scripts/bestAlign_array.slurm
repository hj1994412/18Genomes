#!/bin/bash

#bestAlign.slurm  

#SBATCH -J bestAlign
#SBATCH -n 1
#SBATCH -t 00:20:00
#SBATCH --mem=10000
#SBATCH -p serial_requeue
#SBATCH -o bestAlign%A_%a.out
#SBATCH -e bestAlign%A_%a.err


grep flattened h_melpomene.part-${SLURM_ARRAY_TASK_ID}_alns.maf |\
 awk '{print $2}' |\
 sort -u  > $GENOMES/${SLURM_ARRAY_TASK_ID}_tmp.txt

bestAlignment.py $GENOMES/${SLURM_ARRAY_TASK_ID}_tmp.txt h_melpomene.part-${SLURM_ARRAY_TASK_ID}_alns.maf h_melpomene.part-${SLURM_ARRAY_TASK_ID}_bestAlign.maf

rm $GENOMES/${SLURM_ARRAY_TASK_ID}_tmp.txt

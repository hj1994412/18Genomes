#!/bin/bash
#
# genomeAlign_last.slurm from tophat.sh example
#

#SBATCH -J lastal         # A single job name for the array
#SBATCH -p serial_requeue # Partition
#SBATCH -n 1              # one core
#SBATCH -N 1              # on one node
#SBATCH -t 48:00:00         # Running time of 48 hours
#SBATCH --mem 10000        # Memory request of 10 GB
#SBATCH -o outs/lastal%A_%a.out # Standard output
#SBATCH -e errs/lastal%A_%a.err # Standard error


reference=$1
species=$2 

refLoc=$GENOMES/results/$reference
partsLoc=$GENOMES/data/alignments_fasta/$species/parts_ge1000/$species.part-${SLURM_ARRAY_TASK_ID}.fasta
alignOut=$species/$species.part-${SLURM_ARRAY_TASK_ID}_alns.maf

discoData=$GENOMES/data/alignments_fasta/$species/$species\_clipped_1000.fasta


mkdir -p $species
mkdir -p $species/beds

#find local alignments between query sequences and reference sequences
lastal -m 1000 $refLoc $partsLoc | maf-sort.sh > $alignOut 
cd $species/beds
mafToBed.py ../../$alignOut $discoData

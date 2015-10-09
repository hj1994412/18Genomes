#!/bin/bash

#combineBest.slurm
#take the best alignment from each scaffold and combine them, sort them, and make a dotplot

#SBATCH -p serial_requeue # Partition
#SBATCH -n 4              # one core
#SBATCH -N 5              # on one node
#SBATCH -t 0-12:00         # Running time of 12 hours
#SBATCH --mem 50000        # Memory request of 50 GB
#SBATCH -o combineBest.out # Standard output
#SBATCH -e combineBest.err # Standard error


for file in *_alns.maf
do 
  echo $file
  grep flattened $file | awk '{print $2}' | uniq > $GENOMES/$filetmp.txt
  bestAlignment.py $GENOMES/$filetmp.txt $file $file\_bestAlign.maf
  rm $GENOMES/$filetmp.txt
done

echo "Made all bestAlign files"

#cat *best* | maf-sort.sh > bestAligns.maf

#echo "Made sorted bestAlign file"

#last-dotplot.py bestAligns.maf bestAligns.png

#!/bin/bash

#combineBest.sh
#take the best alignment from each scaffold and combine them, sort them, and make a dotplot


for file in *_alns.maf
do 
  echo $file
  sbatch bestAlign.slurm $file 
  sleep 1
done

echo "Made all bestAlign files"

cat *best* | sbatch mafSort.slurm > bestAligns.maf

echo "Made sorted bestAlign file"

sbatch lastDotplot.slurm bestAligns.maf

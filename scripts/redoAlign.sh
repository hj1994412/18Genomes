#!/bin/bash

#redoAlign.sh

#redo alignments that didn't work with -m 100 on 17 Aug

#take all numbers that didn't work
for file in $var1
do
#print the number
echo $file
#align each one. the -J is job name
sbatch -J align_$file genomeAlign_last.slurm $file
done



#log

#!/bin/bash

#redoAlign.sh

#redo alignments that didn't work with -m 100 on 17 Aug

#take all numbers that didn't work
for file in 12 73 74 80 81 82 111 112 113 202 203 204 208 209 210 474 475 476 477 478 479
do
#print the number
echo $file
#align each one. the -J is job name
sbatch -J align_$file genomeAlign_last.slurm $file
done


cat $GENOMES/scripts/redoAlign.sh | sed -e "s/#log/$(date +'%y%m%d %R')/"  >> $GENOMES/logfile.txt

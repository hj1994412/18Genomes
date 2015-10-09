#!/bin/bash

#SBATCH -p serial_requeue
#SBATCH -n 1
#SBATCH -N 1
#SBATCH -t 0-03:00
#SBATCH --mem=500
#SBATCH -o clipAndSplit.out
#SBATCH -e clipAndSplit.err


cutoff=1000

for s in e_tales h_besckei h_burneyi h_cydno h_demeter h_elevatus h_erato h_erato_himera_hybrid h_hecale h_himera h_melpomene h_numata h_pardalinus h_telesiphe h_timareta l_doris n_aoede
   do
      echo $s
      cd $s/
      removeSmallScaffolds.py $s.fasta $s $cutoff
      mkdir -p parts_ge$cutoff
      cd parts_ge$cutoff/
      fasta-splitter.pl --n-parts 500 ../$s\_clipped_$cutoff.fasta
      cd ../../
      sleep 1
   done  

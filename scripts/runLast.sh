#First, configure reference sequence

sbatch genomeBuild_last.slurm

sbatch fastaSplit.slurm

#Submit the batch job to slurm
n = ls <splitFastaDirectory> | wc -l #Count number of splits (if needed?)
sbatch --array=1-$n genomeAlign_last.sbatch #submit job

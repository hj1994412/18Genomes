#First, configure reference sequence

sbatch genomeBuild_last.slurm

#Use some sort of fasta splitter to make a directory that contains split fasta files
#of h_melpomene fasta (or efasta??) discovar assembly

#Submit the batch job to slurm
n = ls <splitFastaDirectory> | wc -l #Count number of splits (if needed?)
sbatch --array=1-$n genomeAlign_last.sbatch #submit job
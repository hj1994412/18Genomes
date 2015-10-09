for s in e_tales h_besckei h_burneyi h_cydno h_demeter h_elevatus h_erato h_erato_himera_hybrid h_hecale h_himera h_numata h_pardalinus h_telesiphe h_timareta l_doris n_aoede
do
	echo $s
	cd $s/
	mkdir parts
	cd parts/
	sbatch  fastaSplit.slurm ../$s.fasta
	cd ../../
	sleep 1
done  

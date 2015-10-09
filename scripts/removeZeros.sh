for s in a_vanillae e_tales h_besckei h_burneyi h_cydno h_demeter h_elevatus h_erato h_erato_himera_hybrid h_hecale h_himera h_melpomene h_numata h_pardalinus h_telesiphe h_timareta l_doris n_aoede
do
        echo $s
        cd $GENOMES/data/alignments_fasta/$s/parts_ge1000/
        for i in $(seq -f "%03g" 1 500);do j=`echo $i |sed 's/^0*//'`;mv $s\_clipped_1000.part-${i}.fasta $s.part-${j}.fasta;done
done  

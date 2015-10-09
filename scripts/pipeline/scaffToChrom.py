#!/bin/env python

origin=open("Hmel2.fa_copy")
output=open("Hmel2_chromosomes.fa","w")
currentChrom=''
for line in origin:
    if '>' in line:
        chrom=line.split()[0][1:8]
        if chrom != currentChrom:
            output.write('>'+chrom+'\n')
            currentChrom=chrom
        else:
            output.write('N'*100)
    else:
        output.write(line)
            

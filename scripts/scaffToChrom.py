origin=open("Reference/Hmel2_2015-07-17/Hmel2.fa")
output=open("Reference/Hmel2_chromosomes.fa","w")
currentChrom=''
for line in origin:
    if '>' in line:
        chrom=line.split()[0][1:8]
        if chrom != currentChrom:
            output.write('>'+chrom+'\n')
            currentChrom=chrom
        else:
            output.write('N'*60)
            output.write('N'*60)
    else:
        output.write(line)
            
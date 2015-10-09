#!/bin/env python

from Bio import SeqIO
import sys
import csv

def write_csv(file, asequence, header=None):
    fp =  open(file, 'w')
    a = csv.writer(fp, delimiter=',')
    if header:
        a.writerows(header)
    a.writerows(asequence)
    fp.close()


'''takes a concatenated MAF file of the best hits for each contig. The 
alignments must be sorted by their position on the reference sequence'''

bests=open(sys.argv[1])
bread=bests.read()
baligns=bread.split('\n')

chromDict = {}
#Order the 
for index in range(len(baligns)):
    if 'Hmel' in baligns[index]:
        chrom=baligns[index].split()[1][:-3]
        scaf=baligns[index+1].split()[1]
        if not chrom in chromDict.keys():
            chromDict[chrom]=[scaf,]
        else:
            chromDict[chrom].append(scaf)


fasta_file = sys.argv[2] # Input fasta file


for chrom in chromDict.keys():
    name = "pseudo"+str(chrom)
    with open(name+".fa", "w") as f:
        label="> "+str(chrom)+"\n"
        f.write(label)
        thisDict={}
        toCsv=[]
        sPos=0
        ePos=0
        fasta_sequences = SeqIO.parse(open(fasta_file),'fasta')
        for seq in fasta_sequences:
            if seq.id in chromDict[chrom]:
                thisDict[seq.id] = seq.seq
        for scaf in chromDict[chrom]:  
            f.write(str(thisDict[scaf]))
            f.write(str("N"*100)) 
            ePos += (len(str(thisDict[scaf])) + 101)
            toCsv.append([str(scaf), sPos, ePos-101, len(str(thisDict[scaf]))])
            toCsv.append(["Ns", ePos-100, ePos, 100])  
            sPos=ePos+1       
    f.close()
    write_csv(name+".csv",toCsv, header=[["Contig","Start","End","Length"]])

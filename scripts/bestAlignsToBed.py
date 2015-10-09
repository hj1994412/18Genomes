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


bests=open(sys.argv[1])

conDict={}
current=[]
for line in bests:
    if line[0] =='a':
        if current != []:
            conDict[contig]=[scaf,chromStart-conStart,0,contig,chromEnd-chromStart,strand,chromStart,chromEnd,color]
        current=["occupied"]
    elif "Hmel" in line:
        chline=line.split()
        chrom=chline[1][:-3]
        scaf=chline[1]
        chromStart=int(chline[2])
        chromEnd=chromStart+int(chline[3])
       
    elif "flattened" in line:    
        coline=line.split()
        contig=coline[1]
        conStart=int(coline[2])
        conEnd=conStart+int(coline[3])       
        strand = coline[4]
       
d = SeqIO.parse(sys.argv[2], "fasta")
for record in d:
    try:
        conDict[record.id][2]=len(record)+conDict[record.id][1]
        length=conDict[record.id][4]
        score=(float(length)/len(record))*1000
        conDict[record.id][4]=score
        if score > 500:
              conDict[record.id][8]="0,200,0"
        elif score > 250:
              conDict[record.id][8]="128,255,0"
        elif score > 125:
              conDict[record.id][8]="255,255,51"
        elif score > 67:
              conDict[record.id][8]="255,153,51"
        else:
	      conDict[record.id][8]="255,0,0"
    except KeyError:
        pass

bestDict={}
for key in conDict.keys():
    entry=conDict[key]
    bestDict[key]=[entry[0],entry[6],entry[7],entry[3],entry[4],entry[5]]

def writeBed(adict,file):
    with open(file, "w") as f:
        for key in adict.keys():
            bedString=''
            for item in adict[key]:
                bedString+= (str(item) + ' ')
            f.write(bedString + "\n")

file1=sys.argv[3]+"full.bed"
file2=str(sys.argv[3])+"best.bed"

writeBed(conDict,file1)
writeBed(bestDict,file2)
    


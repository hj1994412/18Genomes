#!/bin/env python

from Bio import SeqIO
import sys
import csv
from operator import itemgetter

mafAlignment=sys.argv[1]
base=(mafAlignment.split("/")[-1])[:-4]
discoOutput=sys.argv[2]



def write_csv(file, asequence, header=None):
    fp =  open(file, 'w')
    a = csv.writer(fp, delimiter=',')
    if header:
	a.writerows(header)
    a.writerows(asequence)
    fp.close()


bests=open(mafAlignment)

#Sort the file into individual contigs

conDict={}
current=[]
id=0
for line in bests:
    if line[0] =='a':
        if current != []:
            try:
                conDict[contig].append([scaf,chromStart,chromEnd,id,length,strand,chromStart,chromEnd,0])
            except KeyError:
                conDict[contig]=[[0,0,0,0,0,0,0,0,0],[scaf,chromStart,chromEnd,id,length,strand,chromStart,chromEnd,0]]
            if length > conDict[contig][0][4]:
                conDict[contig][0]=[scaf,chromStart-conStart,0,contig,length,strand,chromStart,chromEnd,0]
        current=["occupied"]
    elif "Hmel" in line:
        chline=line.split()
        chrom=chline[1][:-3]
        scaf=chline[1]
        chromStart=int(chline[2])
        chromEnd=chromStart+int(chline[3])
        length=chromEnd-chromStart

    elif "flattened" in line:
        coline=line.split()
        id += 1
        conStart=int(coline[2])
        conEnd=conStart+int(coline[3])
        strand = coline[4]
        contig=coline[1]

d = SeqIO.parse(discoOutput, "fasta")
for record in d:
    if record.id in conDict.keys():
        for entry in conDict[record.id]:
            if type(entry[3]) == str:
                entry[2]=len(record)+entry[1]
            else:
                length=entry[4]
                score=(float(length)/len(record))*1000
                entry[4]=score
                if score > 500:
                    entry[8]="0,200,0"
                elif score > 250:
                    entry[8]="128,255,0"
                elif score > 125:
                    entry[8]="255,255,51"
                elif score > 67:
                    entry[8]="255,153,51"
                else:
                    entry[8]="255,0,0"

for contig in conDict.keys():
    overall=conDict[contig][0]
    conStart=overall[1]
    conEnd=overall[2]
    chrom=overall[0]
    include=[overall,]
    allInside=True
    sameChrom=True
    sort=sorted(conDict[contig], key=itemgetter(4), reverse=True)
    sumChrom=0
    sumInside=0
    sumLength=0
    for entry in range(len(sort)):
        if sumLength < 950:
            if type(sort[entry][3]) == int:
                include.append(sort[entry])
                sumLength+=sort[entry][4]
                if sort[entry][0] != chrom:
                    sameChrom=False
                else:
                    sumChrom+=sort[entry][4]
                    if sort[entry][1] - conStart < -250:
                        allInside=False
                    elif sort[entry][2] - conEnd > 250:
                        allInside=False
                    else:
                        sumInside += sort[entry][4]
       			if len(include) == 2 and sumLength>=950:
                            for repeat in range(entry+1,len(sort)):
				if sort[repeat][4] >= 900:
				    include.append(sort[repeat])
                                    sumLength+=sort[repeat][4]
				    allInside=False
				else:
				    break
                    

        else:
            if len(include) == 2:
                include[0][8]="0,204,0"
                include[0][4]=1000
            elif allInside:
                include[0][8]="128,255,0"
                include[0][4]=900
            elif sumLength >= 1900:
                if len(include) == 3:
		    include[0][8]="51,255,255"
                    include[0][4]=400
		elif len(include) <=5:
                    include[0][8]="0,128,255"
                    include[0][4]=300
                else:
                    include[0][8]="0,0,204"
                    include[0][4]=200

            elif sumInside>=750:
                include[0][8]="255,255,0"
                include[0][4]=800
            elif sumInside>=500:
                include[0][8]="255,153,51"
                include[0][4]=700
            elif sumChrom>=750:
                include[0][8]="255,102,102"
                include[0][4]=600
            else:
                include[0][8]="204,0,0"
                include[0][4]=500
            f=open(contig+".bed", "a+")
            for i in range(len(include)):
                toWrite=""
                for j in range(len(include[i])-1):
                    toWrite+=(str(include[i][j])+"\t")
                toWrite+=(str(include[i][-1]+"\n"))
                f.write(toWrite)
            break
            



            





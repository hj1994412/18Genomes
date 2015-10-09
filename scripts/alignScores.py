#!/bin/env python

import csv
import sys

def write_csv(file, asequence, header=None):
    fp =  open(file, 'w')
    a = csv.writer(fp, delimiter=',')
    if header:
	a.writerows(header)
    a.writerows(asequence)
    fp.close()

sfile=open(sys.argv[1])

conDict={}
current=[]
for line in sfile:
    if line[0] =='a':
        if current != []:
            try:
                conDict[contig].append(current)	
            except KeyError:
                conDict[contig]=[current,]
        scores=line.split()
        current=[0,str(scores[1])[6:],str(scores[2])[4:], str(scores[3])[2:]]
        
    elif "flattened" in line:
        coline=line.split()
        contig=coline[1]
        current[0]=coline[3]

for scaf in conDict.keys():
    write_csv(str(scaf)+".csv",conDict[scaf], header=[["length","score","EG2","E"]])

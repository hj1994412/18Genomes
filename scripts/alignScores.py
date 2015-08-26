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
sread=sfile.read()
scafs=sread.split('\n')


afile=open(sys.argv[2])
aread=afile.read()
aligns=aread.split('\n')

scafDict={}
for scaf in scafs:
    scafDict[scaf]=[]
    for index in range(len(aligns)):
        if scaf in aligns[index]:
            aline=aligns[index-2]
            scores=aline.split()
            hitline=aligns[index]
            atts=hitline.split()
            scafDict[scaf].append([atts[3],str(scores[1])[6:],str(scores[2])[4:], str(scores[3])[2:]])
    write_csv(str(scaf)+".csv",scafDict[scaf], header=[["length","score","EG2","E"]])

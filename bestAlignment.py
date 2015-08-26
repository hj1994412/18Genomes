#!/bin/env python

import sys

sfile=open(sys.argv[1])
sread=sfile.read()
scafs=sread.split('\n')


afile=open(sys.argv[2])
aread=afile.read()
aligns=aread.split('\n')

toWrite=''

scafDict={}
maxes={}
for scaf in scafs:
    scafDict[scaf]=[]
    for index in range(len(aligns)):
        if scaf in aligns[index]:
            hitline=aligns[index]
            atts=hitline.split()
            scafDict[scaf].append(atts[3])
for s in scafDict:
    maxes[s]=max(scafDict[s])
for m in maxes:
    for index in range(len(aligns)):
        if m in aligns[index] and maxes[m] in aligns[index]:
            toWrite.append(str(aligns[index-2])+'\n'+str(aligns[index-1])+'\n'+str(aligns[index])+'\n')

outfile=open(sys.argv[3],"w")
outfile.write(toWrite)
outfile.close()


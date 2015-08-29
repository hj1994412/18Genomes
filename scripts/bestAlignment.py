#!/bin/env python

import sys

sfile=open(sys.argv[1])
sread=sfile.read()
scafs=sread.split('\n')[:-1]


afile=open(sys.argv[2])
aread=afile.read()
aligns=aread.split('\n')


maxes={}
bests=''
for header in aligns[:19]:
    bests+=str(header)+"\n"

for scaf in scafs:
    maxes[scaf]=0
    best=''
    for index in range(len(aligns)):
        if scaf in aligns[index]:
            hitline=aligns[index]
            atts=hitline.split()
            seqLength=int(atts[3])
            if seqLength > maxes[scaf]:
                maxes[scaf]=seqLength
                best=aligns[index-2]+"\n"+aligns[index-1]+"\n"+aligns[index]+"\n\n"
    bests+=best
                


outfile=open(sys.argv[3],"w")
outfile.write(bests)
outfile.close()

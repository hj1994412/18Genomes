#!/bin/env python

import sys
import csv

maxes={}
scaf=''
with open(sys.argv[2]) as aligns:
    for line in aligns:
        if 'flattened' in line:
            scaf=line.split()[1]
            length=int(line.split()[3])
            if scaf in maxes.keys():
                if length > maxes[scaf]:
                    maxes[scaf]=[length]
            else:
                maxes[scaf]=[length]            

print "Done with alignments"

maxTwo={}
s=''
count=0
mark=0

with open(sys.argv[1]) as reads:
    for read in reads:
        count+=1
        if '>' in read:
            if s != '':
                maxTwo[s]=(count-mark)*60
            mark=count
            s=read[0][1:]
            print s

print "Done with reads"

eachLength=[]
eachLengthTwo=[]
for two in maxTwo:
    eachLengthTwo.append([two, maxTwo[two]])

for m in maxes:
    try:
        eachLength.append([m,maxes[m],maxTwo[m]])
    except KeyError:
        eachLength.append([m,maxes[m],"NA"])
            
def write_csv(file, asequence, header=None):
    fp =  open(file, 'w')
    a = csv.writer(fp, delimiter=',')
    if header:
        a.writerows(header)
    a.writerows(asequence)
    fp.close()
    
write_csv(sys.argv[3]+".csv",eachLength)
write_csv(sys.argv[3]+"Two.csv", eachLengthTwo)

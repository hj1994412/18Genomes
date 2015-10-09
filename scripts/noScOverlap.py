#!/bin env python

import csv
import sys


def checkOverlap(alignment,scoreDict,alignDict):
    #read in the alignment and assign different parts to different variables
    aLine=alignment[0]
    refLine=alignment[1]
    querLine=alignment[2]
    scaf=querLine[1]
    q=[int(querLine[2]),int(querLine[3])]
    
    #reject any very small matches
    if q[1] > 250:
        #check to see if the contig is already in the dictionary. If not, add it with this alignment as the first entry
        if not scaf in scoreDict.keys():
                scoreDict[scaf]=[q,]
                alignDict[scaf]=[alignment,]
        #if the contig is in the dictionary, we need to see if it overlaps an existing alignment
        if scaf in scoreDict.keys():
            keep = True
            #for each of the alignments in the dictionary, check to see if the current alignment overlaps with them
            for index in range(len(scoreDict[scaf])):
                t=scoreDict[scaf][index]
                #if they overlap, don't keep the query, and break the loop
                if (q[0] > t[0] and q[0] < sum(t)) or (sum(q) > t[0] and sum(q) < sum(t)):
                    keep = False 
                    break
            #if the query didn't overlap with anything, keep it.
            if keep == True:
                scoreDict[scaf].append(q)
                alignDict[scaf].append(alignment)
 

alignDict={}
scoreDict={}
thisAlign=[]
#go line by line through maf file
with open(sys.argv[1]) as f:
        for line in f:
                #find the first line of an alignment
                if 'score' in line:
                        if thisAlign != []:
                                checkOverlap(thisAlign,scoreDict,alignDict)
                        thisAlign=[line.split(),]
                elif not '#' in line:
                        thisAlign.append(line.split())



import csv
def write_csv(file, asequence, header=None):
    fp =  open(file, 'w')
    a = csv.writer(fp, delimiter=',')
    if header:
	a.writerows(header)
    a.writerows(asequence)
    fp.close()

toWrite=[]
for key in scoreDict.keys():
    for i in range(len(scoreDict[key])):
        toWrite.append([key,]+scoreDict[key][i])


name=str(sys.argv[1])+"noScOverlap.maf"
indAligns=open(name,"w")
for key in alignDict.keys():
    for i in range(len(alignDict[key])):
        done=''
        for j in range(len(alignDict[key][i])-1):
            line=''
            for k in alignDict[key][i][j]:
                line += k+'\t'
            line += '\n'
            done += line
        indAligns.write(done+'\n')
indAligns.close()

#write_csv(str(sys.argv[1])+'noScOverlap.csv',sorted(toWrite))

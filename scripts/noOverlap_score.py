#!/bin/env python

#updated 9/8 to use the DISCOVAR contig as the basis for overlap vs non-overlap instead of chromosome. This way, each part of the contig is mapped only once, to its best match.

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
        #if the contig is in the dictionary, we need to see if this alignment is better than an overlapping one already there
        if scaf in scoreDict.keys():
            keep = False
            realKeep = True
            #Not an efficient method, but make a blank list, and put every non-overlapping alignment into it
            scopy=[]
            acopy=[]
            #for each of the alignments in the dictionary, check to see if the current alignment overlaps with them
            for index in range(len(scoreDict[scaf])):
                t=scoreDict[scaf][index]
                #if they overlap, check to see which one is bigger
                big = q
                small = t
                if small[1] > big[1]:
                    big = t
                    small = q
                if (small[0] >= big[0] and small[0] <= sum(small)) or (sum(small) >= big[0] and sum(small) <= sum(big)):
                    #if the query is bigger, mark it for a keeper
                    if q[1] > t[1]:
                        keep = True
                    #if the current entry is bigger, add it to the copy, and note that even if the query was bigger than something earlier, 
                    #we don't want it because it's smaller than this.
                    else:
                        scopy.append(t)
                        acopy.append(alignDict[scaf][index])
                        realKeep = False
                #if they don't overlap,, keep both of them
                else:
                    keep = True
                    scopy.append(t)
                    acopy.append(alignDict[scaf][index])

            if keep == True and realKeep == True:
                scopy.append(q)
                acopy.append(alignment)
            #replace the old dictionary entry with the new list
            scoreDict[scaf] = scopy
            alignDict[scaf] = acopy

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



indAligns=open("noOverlap.maf","w")
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

write_csv('noOverlap.csv',sorted(toWrite))

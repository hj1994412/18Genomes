#!/bin/env python

#get all non-overlapping hits that pass a certain threshold

import sys

    
    
    
def checkOverlap(alignment,scoreDict,alignDict):
    overlap=False
    aLine=alignment[0]
    refLine=alignment[1]
    querLine=alignment[2]
    scaf=querLine[1]
    start=int(refLine[2])
    length=int(refLine[3])
    end=start+length
    chrom=refLine[1]
    if length > 250:
        if not scaf in scoreDict.keys():
        	scoreDict[scaf]=[[start,length,chrom],]
        	alignDict[scaf]=[alignment,]
        if scaf in scoreDict.keys():
            scopy=scoreDict[scaf]
            acopy=alignDict[scaf]
            for index in range(len(scoreDict[scaf])):
                tStart=scoreDict[scaf][index][0]
                tLength=scoreDict[scaf][index][1]
                tEnd=tStart+tLength
                tChrom=scoreDict[scaf][index][2]
                if tChrom == chrom:	
                    if (start > tStart and start < tEnd) or (end > tStart and end < tEnd):
                        if tLength > length:
                            overlap = True
                        else:
                            scopy.append(scoreDict[scaf][index])
                            acopy.append(scoreDict[scaf][index])
                    else:
                        scopy.append(scoreDict[scaf][index])
                        acopy.append(scoreDict[scaf][index])
                else:
                    scopy.append(scoreDict[scaf][index])
                    acopy.append(scoreDict[scaf][index])
            scoreDict[scaf] = scopy
            alignDict[scaf] = acopy           
        if overlap == False:
            alignDict[scaf].append(alignment)
            scoreDict[scaf].append([start,length,chrom])
                    
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
	


outfile=open("noOverlap_chrom.maf","w")
for key in alignDict.keys():
    for i in alignDict[key]:
    	for j in alignDict[key][i]:
    		line=''
    		for k in alignDict[key][i][j]:
    			line+=k+'\t'
        	outfile.write(alignDict[key][line]+'\n')
outfile.close()

#!/bin/env python

#bestAlignment.py
#Take an alignment file in maf format and write a new maf file with only the 
#best hit for each query contig

import sys

afile=sys.argv[1]

def bestAligns(mafFile):
    '''Take a file of alignments in maf format 
       Return a maf file with only the best hit for each query contig'''
    f=open(mafFile)
    
    #initialize variables
    maxes={}
    thisAlign=''
    slines=[]
    for line in f:
        #This can be improved...at the beginning of each loop, see if you 
        #already have a full alignment (2 's' entries). 
        if len(slines) == 2:
            #If so, check to see whether the alignment is better than
            #the current best alignment for the contig
            if contig in maxes.keys():
                if alignScore > maxes[contig][0]:
                    thisAlign=aline+slines[0]+slines[1]+"\n"
                    maxes[contig] = [alignScore, thisAlign]
            #If this is the first alignment seen for this contig, make it the 
            #current best alignment
            else:
                thisAlign=aline+slines[0]+slines[1]+"\n"
                maxes[contig]=[alignScore,thisAlign]
        #If the current line is the start of an alignment, clear the "s lines"
        #and record the score
        if line[0] == 'a':
            aline = line
            slines=[]
            atts=aline.split()
            alignScore = int(atts[1][6:])
        #add the 's' lines to the current alignment. If this is the 's' line that 
        #contains the query contig - denoted by "flattened_line_XXXX" - record the 
        #contig label
        elif line[0] == 's':
            slines.append(line)
            satts=line.split()
            if 'flattened' in satts[1]:
                contig=satts[1]
    return maxes

def writeMaf(maxesDict):
    '''write a maf file from the dictionary created by bestAligns'''
    outfile=open(sys.argv[2],"w")
    for key in maxesDict.keys():
        outfile.write(maxesDict[key][1])
    outfile.close()


#execute
writeMaf(bestAligns(afile))

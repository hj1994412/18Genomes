#!/bin/env python

import sys
import csv
#read in the DISCOVAR scaffolds
scaffolds=open(sys.argv[1])

#read in the LAST alignments
aligns=open(sys.argv[2])

# create a dictionary for the results
maxes={}

######
#First, we put in the length of each scaffold
######

#initialize variables for the scaffolds. These will count the lines
#and mark the positions of new scaffolds denoted by ">"
count=0
mark=0
s=""
for line in scaffolds:
    #keep track of the current line
    count+=1
    #find the start of scaffolds
    if '>' in line:
        #ignore the initial values
        if s != "":
            #make an entry into the dictionary with the scaffold name as key
            #and the length of the sequence as value. Also, make a place for the
            #alignment length
            maxes[s]=[((count-1)-mark)*60,0]
        #get the scaffold name
        s=line[1:-1]
        #mark the position of the start of the scaffold
        mark=count

######
#Then, put in the length of the longest alignment
for a in aligns:
    #In this case, the start of an alignment we're interested in is marked by the 
    #scaffold name, which always starts with "flattened"
    if 'flattened' in a:
        scaf=a.split()[1]
        length=int(a.split()[3])
        try:
            if length > maxes[scaf][1]:
                maxes[scaf][1]=length
        except KeyError:
            maxes[scaf]=["MISSING??",length]            


eachLength=[]
for m in maxes:
    eachLength.append([m,maxes[m][0], maxes[m][1]])
                

def write_csv(file, asequence, header=None):
    fp =  open(file, 'w')
    a = csv.writer(fp, delimiter=',')
    if header:
        a.writerows(header)
    a.writerows(asequence)
    fp.close()
    
write_csv(sys.argv[3]+".csv",eachLength)

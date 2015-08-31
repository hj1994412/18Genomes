#!/bin/env python
import sys
import csv

reference=open("Hmel2.fa")
count=0
    
refdict={}

scafStarts={}
now=0
for scaffold in reference:
	if '>' in scaffold:
		name=scaffold.split()[0][1:]
		length=int(scaffold.split()[1][7:-1])
		scafStarts[name]=now
		refdict[name]=''
		now+=length
	else:
		refdict[name]+=(scaffold)

chromDict={}
for ag in agp:
	chrom = ag.split()[0]
	ND = ag.split()[4]
	frag = ag.split()[5]
	if chrom in chromDict.keys():
		if ND=="D":
		    chromDict[chrom]+=refdict[frag]
		elif ND=="N":
		    chromDict[chrom]+=("N"*100)
		    
chrFasta=open("Hmel2_chromosomes.fa","w")
for key in chromDict.keys():
    chrFasta.write('>'+key+' length='+str(len(chromDict[key]))+'\n'+chromDict.key)

#get all non-overlapping hits that pass a certain threshold

import sys


afile=open("h_melpomene.part-100_alns.maf")
aread=afile.read()
aligns=aread.split('\n')

scaffolds={}

#go line by line through maf file
for index in range(len(aligns)):
    if 'score' in aligns[index]:
        aLine=aligns[index].split()
        refLine=aligns[index+1].split()
        querLine=aligns[index+2].split()
        scaf=querLine[1]
        start=int(refLine[2])
        length=int(refLine[3])
        end=start+length
        if scaf in scaffolds.keys():
            for entry in scaffolds[scaf]:
                test=entry.split('\n')
                tRefLine=test[1].split()
                tStart=int(tRefLine[2])
                tLength=int(tRefLine[3])
                tEnd=tStart+tLength
                if start > tStart and start < tEnd:
                    if tLength < length:
                        scaffolds[scaf].remove(entry)
                        scaffolds[scaf].append(aligns[index]+"\n"+aligns[index+1]+"\n"+aligns[index+2]+"\n\n")
                elif end > tStart and end < tEnd:
                    if tLength < length:
                        scaffolds[scaf].remove(entry)
                        scaffolds[scaf].append(aligns[index]+"\n"+aligns[index+1]+"\n"+aligns[index+2]+"\n\n")
                else:
                    scaffolds[scaf].append(aligns[index]+"\n"+aligns[index+1]+"\n"+aligns[index+2]+"\n\n")
        else:
            scaffolds[scaf]=[aligns[index]+"\n"+aligns[index+1]+"\n"+aligns[index+2]+"\n\n",]

outfile=open("noOverlap_chrom.maf","w")
for key in scaffolds.keys():
    for i in scaffolds[key]:
        outfile.write(i)
outfile.close()
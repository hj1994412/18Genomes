import csv
def write_csv(file, asequence, header=None):
    fp =  open(file, 'w')
    a = csv.writer(fp, delimiter=',')
    if header:
        a.writerows(header)
    a.writerows(asequence)
    fp.close()

alignment=open('h_melpomene.fasta')
nlines=0
count=0
scaffolds = {}

for line in alignment:
    if '>' in line:
        baseCount=0
        scaffolds[str(line)] = 0
        current=str(line)
        count += 1
        nlines += 1
    else:
        scaffolds[current] += len(line)
        nlines += 1
mydict={}
for i in range(50):
    mydict[i*25]=0
for scaf in scaffolds:
    for key in mydict:
        if scaffolds[scaf] >= key:
            mydict[key] += 1

densityOut=[]
for key in mydict:
    densityOut.append([key,mydict[key],float(mydict[key])/mydict[0]])
    
distribOut=[]
for key in scaffolds:
    distribOut.append([key,scaffolds[key]])


write_csv("InvDensity.csv",sorted(densityOut), header=[["length","numScaffolds","pctScaffolds"]])
write_csv("Distribution.csv", distribOut, header=[["scaffoldID", "length"]])


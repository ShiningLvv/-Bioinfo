#!/usr/bin/python
# -*- coding:utf-8 -*-

floc=open('jieguo.duandian02.NA19819.chrom11.jiqi02','r')
fori=open('/mnt/hdd/liuweiwei/data/03/sam/NA19819.chrom11.sam','r')
fext=open('dd-reads.jiqi02.NA19819.chrom11.fa','w')

L1=[]
L2=[]

line_floc=floc.readlines()
for i in line_floc:
    sb=i.strip().split()
    L1.append(sb[0])
    L2.append(sb[1])

line_fori=fori.readlines()
for eachline in line_fori:
    if(eachline[0]=='@'):
        continue
    #fext.write(eachline)
    elif(eachline=='\r\n'):
        continue
    else:
        sp=eachline.strip().split()
        pos=int(sp[3])
        for i in range(len(L1)):
            if(int(L1[i])-50 < pos < int(L2[i])):
                print >> fext, ">" + sp[0]+"    "+sp[3]+"    "+sp[5]
                print >> fext,sp[9]
                break
floc.close()
fori.close()
fext.close()

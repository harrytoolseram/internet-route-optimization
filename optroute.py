import math

slist=[]
subnet=[]
for line in open('internet-route-subsets.txt','r'):
    temp=line.rstrip('\n\r')
    idata=temp.split('/')
    slist.append(idata[0])
    subnet.append(idata[1])
    print idata[0],' = ',idata[1]
    

#slist=['197.0.0.0','233.23.0.0','233.23.23.0','192.168.100.0','211.0.0.0','211.12.1.0','211.12.0.0','202.12.213.50','202.12.213.0','196.0.0.0','197.213.200.0','197.213.23.0','196.20.20.0','197.213.22.0','197.213.0.0','197.213.23.0']
#subnet=['8','16','24','24','8','24','16','32','24','8','28','24','23','19','16','25']

slist_bin=[]
slistcnt=len(slist)

############################

def dec_to_bin(y):

   listz=[0,0,0,0,0,0,0,0]
   x=7
   while (y > 0):
       listz[x] = y%2
       x-=1
       y=math.trunc(y/2)
   return listz

############################

def list_to_str(listy):

    b=''
    x=0
    while (x < 8):
        b=b+str(listy[x])
        x+=1
    return b

############################

def binary_join(ipadd):

    d=''
    a=ipadd.split('.')
    for i in range(0,4):
#        print a[i]
        list=dec_to_bin(int(a[i]))
        z=list_to_str(list)
        d+=z
#        print list
#        print z
    return d

############################

def sort_bin():

    global slist_bin,slist_sub,subnet,slist,slistcnt

    for i in range (0,slistcnt-1):
#        print 'i = ',i
        for j in range (i+1,slistcnt):
#            print 'j = ',j
            if slist_bin[i] > slist_bin[j]:
                t1=slist_bin[i]
                slist_bin[i]=slist_bin[j]
                slist_bin[j]=t1
                t2=subnet[i]
                subnet[i]=subnet[j]
                subnet[j]=t2
                t3=slist[i]
                slist[i]=slist[j]
                slist[j]=t3
                t4=slist_sub[i]
                slist_sub[i]=slist_sub[j]
                slist_sub[j]=t4
            if ((slist_bin[i]==slist_bin[j]) and (subnet[i]>subnet[j])):
                t1=slist_bin[i]
                slist_bin[i]=slist_bin[j]
                slist_bin[j]=t1
                t2=subnet[i]
                subnet[i]=subnet[j]
                subnet[j]=t2
                t3=slist[i]
                slist[i]=slist[j]
                slist[j]=t3
                t4=slist_sub[i]
                slist_sub[i]=slist_sub[j]
                slist_sub[j]=t4
 
            
############################

def id_superset():

    i=0
    j=i+1
    super=0
    subset=0
    superc=0
    subc=0
    print
    print 'SUPERSET & SUBSET OPTIMIZATION'
    print
    while (i < slistcnt) & (j < slistcnt):
        if slist_bin[i][:int(subnet[i])]==slist_bin[j][:int(subnet[i])]:
	    j+=1
        else:
            print 'Superset:    ' + slist[i] + '/' + subnet[i]
            super=i
            superc+=1
            if ((i+1)<j):
                for h in range (i+1,j):
                    print '     Subset: ' + slist[h] + '/' + subnet[h]
                    subc+=1
                    subset=h
            i=j
            j=i+1

    if (i > super):
        print 'Superset:    ' + slist[i] + '/' + subnet[i]
        superc+=1
    if (j > subset):
        for h in range (i+1,j):
            print '     Subset: ' + slist[h] + '/' + subnet[h]
            subc+=1

    print
    print 'Total superset routes    : ',superc
    print 'Total subset routes      : ',subc
    print 'Total routes             : ',slistcnt
    print
    print 'Route optimization       : ',float(subc)/float(slistcnt)*100,'%'
		

############################
    
slist_sub=[]

for i in range (0,slistcnt):
    slist_bin.append(binary_join(slist[i]))
    print i
    slist_sub.append(slist_bin[i][:int(subnet[i])])

sort_bin()

for i in range (0,slistcnt):
    print 'IP Address:         ' + slist[i]
    print 'Binary version:     ' + slist_bin[i]
    print 'Subnet:             /' + subnet[i]
    print 'After apply subnet: ' + slist_sub[i]
    print

id_superset()

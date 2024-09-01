t=int(input())
while t>0 :
    s1=input()
    s2=input()
    s3=""
    i=0
    j=0
    while i<len(s1) or j <len(s2):
        if i<len(s1) :
            print(s1[i],end="")
            i=i+1

        if j<len(s2) :
            print(s2[j],end="")
            j=j+1 
    t=t-1          

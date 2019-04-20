def MO(L):
    mo=0.0
    for i in range(len(L)):
        mo+=L[i]
    mo=mo/len(L)
    return mo

ON=[]; MIS=[]
for i in range(30):
    x=raw_input("Write your name: ")
    y=input("Write your salary: ")
    while y<500 or y>2000:
        y=input("Salary must be between 500-2000: ")
    ON.append(x)
    MIS.append(y)

z=MO(MIS)
for i in range(len(MIS)):
    if z>MIS[i]:
        t=MIS[i]*0.10+MIS[i]
        MIS.pop(i)
        MIS.insert(i,t)
      
for i in range(len(MIS)-1):
    for j in range(len(MIS)-1,i,-1):
        if MIS[j]>MIS[j-1]:
            MIS[j],MIS[j-1]=MIS[j-1],MIS[j]
            ON[j],ON[j-1]=ON[j-1],ON[j]
        
for i in range(5):
    print 'The number',i+1,'employee with the biggest salary is',ON[i],'with',MIS[i],'$ per month'

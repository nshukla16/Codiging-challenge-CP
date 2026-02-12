#print n times given value
def printf(i,n):
    if(i>n):
        return
    print('rahul')
    # i+=1
    printf(i+1,n)
# printf(1,5)

#print value from 1 to n asc order
def printNumAsc(i,n):
    if(i>n):
        return
    print(i)

    printNumAsc(i+1,n)
# printNumAsc(1,5)

#print value n to 1 dsc order
def printNumDsc(i,n):
    if(i>n):
        return
    
    printNumDsc(i+1,n)
    print(i)

# printNumDsc(1,5)

#sum of given n numbers parameterise way
def printSum(i,sum):
    if(i<1):
        print(sum)
        return
    
    printSum(i-1, sum+i)

#printSum(4,0)

#sum of given n numbers using functional way
def printSumF(i):
    if(i==0):
        return 0
    
    return i + printSumF(i-1)
df = printSumF(4) 
print(df)
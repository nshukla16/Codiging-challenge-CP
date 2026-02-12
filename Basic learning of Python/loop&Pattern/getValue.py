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
printNumAsc(1,5)


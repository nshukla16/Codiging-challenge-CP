def star(n):
    for row in range(1,n+1):
        # print(row)
        for col in range(1,row+1):
            print(col, end=' ')
        print()

star(6)  
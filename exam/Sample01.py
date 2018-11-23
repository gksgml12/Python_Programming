x = int(input())
y = int(input())

for i in range(x,0,-1):
    for j in range(1,y+1):
        if (i>j):
            print(' '*4,end='')
        else:
            print('%4d'%(i*100+(-i+j+1)), end='')
    print()
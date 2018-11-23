x = int(input())

for i in range(x,0,-1):
    mul=1
    for j in range(1, x+1):
        if(i>j):
            print(' '*2,end='')
        else:
            mul*=j
            print('%2d'%j,end='')
    print('%7d'%mul)
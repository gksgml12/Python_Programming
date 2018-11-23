startVList =[]

startVList.append(int(input()))
startVList.append(int(input()))
startVList.append(int(input()))
startVList.append(int(input()))
startVList.append(int(input()))
sec = int(input())

BList =[]
HList = [90, 80, 91, 99, 70]

for i in range(5):
    if ((startVList[i]+(sec*HList[i]))//2000)<1:
        r = startVList[i] + sec*HList[i]
    else:
        sec-=(2000-startVList[i])//HList[i]
        r = sec*HList[i]
    if r==0:
        r=2000
    BList.append(r)

maxV = max(BList)
print('%2d,%5d'%(BList.index(maxV)+1, maxV))
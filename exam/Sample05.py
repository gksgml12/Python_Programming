x = input()

result =[]

for v1 in x:
    if v1.isalpha():
        result.append(v1.lower())

comStr = result.copy()
comStr.reverse()

if result==comStr:
    print(1,end='')
else:
    print(0,end='')

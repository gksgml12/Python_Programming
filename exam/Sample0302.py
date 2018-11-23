x = input()

result=''
sum =0
mlist='aeiou'

for v1 in x:
    if v1.isalnum():
        if v1 in mlist:
            result = result+'M'+v1
        elif v1.isnumeric():
            sum+=int(v1)
        else:
            result = result+v1+'J'

print('%7d, %s'%(sum,result))




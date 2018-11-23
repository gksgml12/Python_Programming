f1 = open('miro.txt','r')
data = f1.readlines()

maze = {}

for str1 in data:
    temp= str1.strip('\n')
    maze[temp[0]] = list(temp[1:])

print(maze)

def solve(g, start, end):
    qu =[] #다음에 갈수 있는 경로를 저장
    done=set() #중복 방지를 위한 집합

    qu.append(start) # 출발점에 출발
    done.add(start) # 출발점을 집합에 추가

    while qu:
        p=qu[0] #큐에서 처리 대상을 꺼냄
        qu.remove(p) #큐에서 꺼낸것 삭제
        v=p[-1] #큐중에서 마지막 것이 처리해야 할 것
        if v==end: # 목적지이면 종료
            return p
        for x in g[v]: #연결된 경로(점)를 돔
            if x not in done: #큐에 추가된 적이 있는지, 없는지 판단
                qu.append(p+x) #이동경로에 새 점을 추가하여 큐에 저장
                done.add(x) #집합에도 추가


print(solve(maze, 'a','p'))
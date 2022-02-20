from collections import deque

def DFS(start, route):
    log = []
    store = [start]
    while store:
        start = store.pop()
        if start not in log:
            log.append(start)
            if start in route:
                tmp = list(set(route[start])-set(log))
                tmp = sorted(tmp, reverse = True)
                store += tmp
        
    return ' '.join(str(i) for i in log)

def BFS(start, route):
    log = []
    store = deque([start])
    while store:
        start = store.popleft()
        if start not in log:
            log.append(start)
            if start in route:
                tmp = list(set(route[start]) - set(log))
                tmp.sort()
                store += tmp

    return ' '.join(str(i) for i in log)

point, line, start = map(int, input().split())

route = {}

for i in range(line):
    point1, point2 = map(int, input().split())
    
    if point1 not in route:
        route[point1] = [point2]
    else:
        route[point1].append(point2)
    
    if point2 not in route:
        route[point2] = [point1]
    else:
        route[point2].append(point1)

print(DFS(start, route))
print(BFS(start, route))


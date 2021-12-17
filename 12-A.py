graph = {}

#fill graph dict
with open("12-input.txt") as file:
    lines = [x.strip() for x in file.readlines()]
    for line in lines:
        start, end = line.split("-")
        if start not in graph.keys():
            graph[start] = []
            graph[start].append(end)
        if end not in graph.keys():
            graph[end] = []
            graph[end].append(start)
    
    for line in lines:
        start, end = line.split("-")
        if start not in graph[end]:
            graph[end].append(start)
        if end not in graph[start]:
            graph[start].append(end)


def find_all_paths(graph:dict, start, end, path=[]): 
    path = path + [start]
    if start == end:
        return [path] 
    if not start in graph.keys():
        return [] 
    paths = [] 
    for node in graph[start]:
        if str(node).islower() and node in path:
            continue #skip on pesky smol caves
        else:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths


allpaths = find_all_paths(graph, "start", "end")

print(len(allpaths))
graph = {}

# fill graph
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


def find_all_paths(graph: dict, start, end, path=[], revisit_smol_cave: bool = False, already_visited_small_cave: bool = False):
    path = path + [start]
    if start == end:
        return [path]
    if not start in graph.keys():
        return []
    paths = []
    for node in graph[start]:
        if str(node).islower() and node in path and not revisit_smol_cave:
            continue  # skip on pesky smol caves
        elif revisit_smol_cave and (str(node) == 'start' or str(node) == 'end'):
            continue
        elif str(node).islower() and node in path and revisit_smol_cave and not already_visited_small_cave:
            newpaths = find_all_paths(graph, node, end, path, False, True)
            for newpath in newpaths:
                paths.append(tuple(newpath))
        else:
            newpaths = find_all_paths(
                graph, node, end, path, False, already_visited_small_cave)
            if not already_visited_small_cave:
                newpaths += find_all_paths(graph, node, end,
                                           path, True, already_visited_small_cave)
            for newpath in newpaths:
                paths.append(tuple(newpath))
    return paths


allpaths = set(find_all_paths(graph, "start", "end"))

print(len(allpaths)) #133360


# def find_path(graph:dict, start, end, path=[]):
#     path = path+[start]
#     if start == end:
#         return path
#     if not start in graph.keys():
#         return None
#     for node in graph[start]:
#         if node not in path:
#             newpath = find_path(graph, node, end, path)
#             if newpath : return newpath
#     return None

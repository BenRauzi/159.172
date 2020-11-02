graph = {'0': ['1', '2'],
         '1': ['0', '3', '4'],
         '2': ['0', '4'],
         '3': ['1', '4'],
         '4': ['1', '2', '3', '5'],
         '5': ['4', '6'],
         '6': ['5']}



def dfs(visited, graph, vertex):
        print (vertex)
        visited.append(vertex)
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                dfs(visited, graph, neighbour)
            
# dfs that stops when it finds the correct vertex. Last item in visited will be the correct vertex
def dfs_stop(visited, graph, vertex, target):
        print(vertex)
        visited.append(vertex) #technically we should 'visit' before we find, in case this list was wanted to be used in some further algorithm. Alternatively we could return the final vertex, but this is not asked

        if vertex == target:
            return True
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                found_target = dfs_stop(visited, graph, neighbour, target)
                if found_target:
                    return True

dfs([], graph, '0')

print() #spacing

dfs_stop([], graph, '0', '4')
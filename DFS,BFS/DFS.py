# def dfs(graph,n,visited):

#     if not(visited[n]):
#         visited[n] = True
#         print(n,end=' ')
#         for i in graph[n]:
#             dfs(graph,i,visited)
#     else:
#         return
    
graph = [
    [],
    [2,3,4],
    [1,7],
    [2,4,5],
    [1,2],
    [1,8],
    [4,7],
    [2,6,8],
    [2,6]
]

visited = [False]*(len(graph))

dfs(graph,1,visited)

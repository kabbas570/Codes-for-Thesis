
def Depth_First_Search(matrix, visited, node):
    visited[node] = True
    for i in range(len(matrix)):
        if matrix[node][i] and not visited[i]: 
            Depth_First_Search(matrix, visited, i)
            
def get_minimum_connections(matrix):
    n = len(matrix)
    visited = [False] * n
    components = 0

    for i in range(n):
        if not visited[i]:  
            Depth_First_Search(matrix, visited, i)
            components += 1
    return components - 1
    

matrix = \
    [ 
        [False, True, False, False, True], 
        [True, False, False, False, False], 
        [False, False, False, True, False], 
        [False, False, True, False, False], 
        [True, False, False, False, False] 
    ]
print(get_minimum_connections(matrix))

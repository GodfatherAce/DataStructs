# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 14:05:13 2021

@author: Sachin Tripathi
"""
# declaring a simple list
l1 = [1, 4, 6, 7, 10]

# membership operators
6 in l1

# identify the location: Linear Search
for i in range(len(l1)):
    if l1[i] == 6:
        print("Element found at index: ", i)

# identify the location: Binary Search
val = 7
first = 0
last = len(l1) - 1
index = -1
while(first <= last) and (index == -1):
    mid = (first + last) // 2
    if(l1[mid] == val):
        index = mid
    else:
        if val < l1[mid]:
            last = mid - 1
        else:
            first = mid + 1
    print(index)

# Implementing Breadth-First Search
# creating a tree-graph structure with parent-child node data

graph = {0: [1, 2], 1: [3, 4], 2: [], 3: [], 4: []}
graph1 = {'R': ['P', 'Q'], 
          'P': ['S'], 
          'Q': ['T', 'M'],
          'S': ['Z'], 
          'T': ['X', 'Y'], 
          'M': ['A'], 
          'Z': [],
          'X': [],
          'Y': [],
          'A':[]
          }

visited = []
queue = []

def bfs(visited, graph, node):
    
    visited.append(node)
    queue.append(node)
    
    while queue:
        s = queue.pop(0)
        print(s, end = " ")
        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
        
# calling the function to simulate the searching        
bfs(visited, graph1, 'Q')
print('\n')

# printing the visited node and queued values
print(visited)
print(queue)

# Implementing Depth-First Search

graph = {'A': ['B', 'C'],
         'B': ['D', 'E'],
         'C': ['F', 'G'], 
         'D': [], 
         'E': [], 
         'F': [],
         'G': []
        }

visited = set()

def dfs(visited, graph, node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)
            
# calling the function to simulate the searching
dfs(visited, graph, 'A')




graph = {'A': ['B', 'C'],
         'B': ['E'],
         'C': ['F'], 
         'E': ['F'], 
         'F': [],
        }

























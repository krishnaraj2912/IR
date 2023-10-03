import numpy as np

graph = {0:[1],1:[0,2],2:[1]}
n = len(graph)
# print(n)

adj_mat = []
for i in graph.values():
  cur = [0]*n
  if len(i) == 0:
    for i in range(n):
      cur.append(1/n)
  else:
    prob = 1/len(i)
    for i in i:
      cur[i] = prob
  
  adj_mat.append(cur)
print(adj_mat)

adj_mat = np.array(adj_mat)
print(adj_mat)

alpha = 0.5
G = (1-alpha)*adj_mat
G += (alpha/n)
print(G)

prev = np.array([1/n]*n)
cur = prev

while True:
  prev = cur
  cur = np.matmul(cur,G)
  flag = 0

  print("Prev =",prev,"\nCur =",cur)
  for i in range(n):
    if cur[i]-prev[i]>0.01:
      # print(cur[i]-prev[i])
      flag = 1
      break
  
  # print(flag)
  if flag == 0:
    break
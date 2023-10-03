import numpy as np

adjMat = [
      [0,0,0,1,0,0,0,0],
      [0,0,1,0,1,0,0,0],
      [1,0,0,0,0,0,0,0],
      [0,1,1,0,0,0,0,0],
      [0,1,1,1,0,1,0,0],
      [0,0,1,0,0,0,0,1],
      [1,0,1,0,0,0,0,0],
      [1,0,0,0,0,0,0,0]
  ]

# adjMat = [
#     [0,1,1,1],
#     [0,0,1,1],
#     [0,1,0,0],
#     [1,0,1,0]
# ]

trans = np.transpose(adjMat)
print(trans)

a = [1]*len(adjMat)
h = a
print(h,a)

old_a = a
old_h = h
while True:
  new_a = (np.matmul(trans,old_h).tolist())
  new_h = (np.matmul(adjMat,old_a).tolist())
  
  flag = 1
  total_sum_a = sum(new_a)*1.0
  total_sum_h = sum(new_h)*1.0
  
  
  for i in range(len(a)):
    # print(total_sum_a,total_sum_h)
    new_a[i] = new_a[i]/total_sum_a
    new_h[i] = new_h[i]/total_sum_h
  
  
  for i in range(len(a)):
    if abs(old_a[i]-new_a[i])>0.01:
      flag = 0
      break
    if abs(old_h[i]-new_h[i])>0.01:
      flag = 0
      break
  
  if flag == 1:
    break
  print("a =",new_a,"\nh =",new_h)
  print("\n")
  
  
  old_a = new_a
  old_h = new_h
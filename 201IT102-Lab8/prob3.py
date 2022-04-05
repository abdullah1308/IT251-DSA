from os import sep
import sys
from disjointsets import DisjointSets

d = {}
ds = DisjointSets()
edges = []
cost = 0
tree = set()

def merge_sort(unsorted_list):
   if len(unsorted_list) <= 1:
      return unsorted_list
    
  # Find the middle point and devide it
   middle = len(unsorted_list) // 2
   left_list = unsorted_list[:middle]
   right_list = unsorted_list[middle:]

   left_list = merge_sort(left_list)
   right_list = merge_sort(right_list)
   return list(merge(left_list, right_list))

# Merge the sorted halves
def merge(left_half,right_half):
   res = []
   while len(left_half) != 0 and len(right_half) != 0:
      if left_half[0][2] < right_half[0][2]:
         res.append(left_half[0])
         left_half.remove(left_half[0])
      else:
         res.append(right_half[0])
         right_half.remove(right_half[0])
   if len(left_half) == 0:
      res = res + right_half
   else:
      res = res + left_half
   return res


# Ensure number of arguments is two    
if len(sys.argv) == 2:
  fname = sys.argv[1]  # Second argument is the file name.
  file=open(fname,'r')
  # Read input line by line
  i = 0
  for line in file: 
    if i == 0:
      n, m = line.strip().split(" ")
      n, m = int(n), int(m)
      for j in range(n):
        d[j] = ds.makeset(j)
    else:
      p1, p2, w = line.strip().split(" ")
      p1, p2, w = int(p1), int(p2), int(w)
      edges.append([p1, p2, w])
    i += 1
  
  edges = merge_sort(edges)
  # print(items)
  
  for edge in edges:
    p1, p2, w = edge
    if ds.findset(d[p1]) == ds.findset(d[p2]):
      continue
    tree.add((p1,p2))
    cost += w
    ds.union(d[p1], d[p2])
  
  print("Edges in MST: ", end="")
  print(str(list(tree))[1:-1])
  print(f"Cost of MST: {cost}")

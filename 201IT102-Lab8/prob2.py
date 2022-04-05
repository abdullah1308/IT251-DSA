import sys
from collections import deque
from sys import maxsize as INT_MAX
from disjointsets import DisjointSets

d = {}
ds = DisjointSets()

# Ensure number of arguments is two    
if len(sys.argv) == 2:
  fname = sys.argv[1]  # Second argument is the file name.
  file=open(fname,'r')
  # Read input line by line
  i = 0
  for line in file: 
    if i == 0:
      n, m, q = line.strip().split(" ")
      n, m, q = int(n), int(m), int(q)
      for j in range(n):
        d[j] = ds.makeset(j)
    elif i <= m:
      p1, p2 = line.strip().split(" ")
      p1, p2 = int(p1), int(p2)
      ds.union(d[p1], d[p2])
    else:
      p1, p2 = line.strip().split(" ")
      p1, p2 = int(p1), int(p2)
      ans = ds.findset(d[p1]) == ds.findset(d[p2])
      print(f"vertex {p1} and {p2}: ", "same" if ans else "different")
    i += 1
import sys

class DisjointSets(object):

  class Node(object):
    def __init__(self, value):
      self.value = value
      self.parent = self
      self.rank = 0

  # Creates a new set containing the single element i by creating a new Node object. Returns the new Node object created.
  def makeset(self, i):
    return self.Node(i)
  
  # Returns the representative element of the set containing node x.
  def findset(self, x): 
    if x.parent.value != x.value:
      xParent = self.findset(x.parent)
      return xParent
    return x
  
  # Unites the two disjoint sets containing node x and y. Return nothing.
  def union(self, x, y):
    xRoot = self.findset(x)
    yRoot = self.findset(y)
    if xRoot == yRoot:
      return
    if xRoot.rank < yRoot.rank:
      xRoot.parent = yRoot
    elif xRoot.rank > yRoot.rank:
      yRoot.parent = xRoot
    else:
      xRoot.parent = yRoot
      yRoot.rank += 1

d = {}
ds = DisjointSets()

# Ensure number of arguments is two    
if len(sys.argv) == 2:
  fname = sys.argv[1]  # Second argument is the file name.
  file=open(fname,'r')
  for line in file: 
    lineSplit = line.strip().split(" ")
    if lineSplit[0] == "m":
      for num in lineSplit[1:]:
        d[num] = ds.makeset(int(num))
        print(f"makeset {num}")
    elif lineSplit[0] == "f":
      num = lineSplit[1]
      val = ds.findset(d[num]).value
      print(f"findset({num}): {val}")
    elif lineSplit[0] == "u":
      xNum, yNum = lineSplit[1], lineSplit[2]
      ds.union(d[xNum], d[yNum])
      print(f"union({xNum},{yNum})")
    
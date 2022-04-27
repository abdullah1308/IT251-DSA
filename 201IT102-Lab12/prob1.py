import heapq
import sys

class BinaryHeap:
    arr=[]

    def heapify(self,arr,i):
        l = self.left(i)
        r = self.right(i)
        if l < len(arr) and arr[l] > arr[i]:
            max = l
        else:
            max = i
        if r < len(arr) and arr[r] > arr[max]:
            max = r
        if max != i:
            arr[i], arr[max] = arr[max], arr[i]
            self.heapify(arr,max)

    def left(self,i):
        return 2*i+1

    def right(self,i):
        return 2*i+2

    def build_heap(self,arr):
        n = int((len(arr)//2)-1)
        for k in range(n,-1,-1):
            self.heapify(arr,k)

    def insert(self,arr,val):
        if len(arr) == 0:
            arr.append(val)
        else:
            arr.append(val);
            n = int((len(arr)//2)-1)
            for k in range(n,-1,-1):
                self.heapify(arr,k)

    def extractMax(self,arr):
        m = arr[0]
        arr[0] = arr[len(arr)-1]
        arr.pop(len(arr)-1)
        self.heapify(arr,0)
        return m

    def print_heap(self,arr):
        print(arr)


def main():
    if len(sys.argv) < 1:
        return

    fname = sys.argv[1]
    file = open(fname, 'r')
    h = BinaryHeap()
    for line in file:
        l = line.split(" ")
        l[len(l)-1] = l[len(l)-1].split("\n")[0]
        if l[0]=='b':
            for i in range(1,len(l)):
                h.arr.append(int(l[i]))
            h.build_heap(h.arr)
            print("Build Heap:",end=" ")
            h.print_heap(h.arr)
        elif l[0]=='e':
            print("Extract Max:",h.extractMax(h.arr),end="; ")
            h.print_heap(h.arr)
        elif l[0]=='i':
            h.insert(h.arr,int(l[1]))
            print("Insert",l[1],":",end=" ")
            h.print_heap(h.arr)
        else:
            print("Invalid!!")

    file.close()


if __name__ == '__main__':
    main()
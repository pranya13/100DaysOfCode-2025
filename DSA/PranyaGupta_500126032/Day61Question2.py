class Solution:
    def __init__(self):
        self.heap = []
    def bubbleUp(self, ind):
        p = (ind-1)//2
        while ind>0 and self.heap[ind]>self.heap[p]:
            self.heap[ind], self.heap[p] = self.heap[p], self.heap[ind]
            ind  = p
            p = (ind-1)//2
    def insert(self, val):
        self.heap.append(val)
        self.bubbleUp(len(self.heap)-1)

    def shiftDown(self, ind):
        n = len(self.heap)
        while True:
            lmax = ind
            l = 2*ind+1
            r = 2*ind+2

            if l<n and self.heap[l]>self.heap[lmax]:
                lmax = l
            
            if r<n and self.heap[r]>self.heap[lmax]:
                lmax = r
            if lmax == ind:
                break
            self.heap[ind], self.heap[lmax] = self.heap[lmax], self.heap[ind]
            ind - lmax
    def deleteRoot(self):
        if not self.heap:
            return None
        root = self.heap[0]
        lst = self.heap.pop()
        if self.heap:
            self.heap[0] = lst
            self.shiftDown(0)
        return self.heap
    def getheap(self):
        return self.heap
def main():
    sol = Solution()
    user_input = input("Enter operations (e.g., Insert 30, Delete root, Insert 40): ")
    operations = [op.strip() for op in user_input.split("→")]

    for op in operations:
        if op.lower().startswith("insert"):
            value = int(op.split()[1])
            sol.insert(value)
        elif op.lower().startswith("delete"):
            sol.delete_root()

    print("Heap after operations:", sol.get_heap())


if __name__ == "__main__":
    main()                                      


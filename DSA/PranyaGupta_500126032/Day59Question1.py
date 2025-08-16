class Solution:
    def __init__(self):
        self.heap = []
    def insert(self, val):
        self.heap.append(val)
        self.bubbleUp(len(self.heap)-1)
    def extractMin(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop() 
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.bubbleDown(0)
        return root       
    
    def bubbleUp(self, i):
        p = (i-1)//2
        while i>0 and self.heap[i] < self.heap[p]:
            self.heap[i], self.heap[p] = self.heap[p], self.heap[i]
            i, p = p, (p-1)//2

    def bubbleDown(self, i):
        n = len(self.heap)
        while True:
            l, r = 2*i+1, 2*i+2
            s = i
            if l<n and self.heap[l]< self.heap[s]:
                s = l
            if r<n and self.heap[r]< self.heap[s]:
                s = r
            if s!=i:
                self.heap[i], self.heap[s] = self.heap[s], self.heap[i]
                i  = s
            else:
                break
def main():
    user_input = input("Enter the elements to insert in the heap (separated by space): ")
    arr = list(map(int, user_input.strip().split()))
    sol = Solution()
    for n in arr:
        sol.insert(n)
    k = int(input("Enter number of times you want to extract min: "))
    res = []
    for i in range(k):
        res.append(sol.extractMin())
    print(res)

if __name__ == "__main__":
    main()                

                 


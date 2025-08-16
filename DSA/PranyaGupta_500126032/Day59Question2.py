import heapq
class Solution:
    def __init__(self):
        self.heap = []
    def insert(self, val):
        heapq.heappush(self.heap, -val)
    def extractMax(self):
        if not self.heap:
            return None
        return -heapq.heappop(self.heap)



def main():
    user_input = input("Enter the elements to insert in the heap (separated by space): ")
    arr = list(map(int, user_input.strip().split()))
    sol = Solution()
    for n in arr:
        sol.insert(n)
    k = int(input("Enter number of times you want to extract min: "))
    res = []
    for i in range(k):
        res.append(sol.extractMax())
    print(res)

if __name__ == "__main__":
    main()                

                 


import heapq
from collections import Counter
class Solution:
    def kfrequentElements(self, arr, k):
        freq = Counter(arr)
        heap = [(-c, n) for n, c in freq.items()]
        heapq.heapify(heap)
        res = []
        for _ in range(k):
            c, n = heapq.heappop(heap)
            res.append(n)
        return res    
        

                         


def main():
    user_input = input("Enter the elements of heap (separated by space): ")
    arr = list(map(int, user_input.strip().split()))
    k = int(input("Enter k: "))
    sol = Solution()
    print(sol.kfrequentElements(arr, k))

if __name__ == "__main__":
    main()                

                 


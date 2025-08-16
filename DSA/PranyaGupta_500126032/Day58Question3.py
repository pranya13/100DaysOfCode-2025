import heapq
class Solution:
    def minHeap(self, arr):
        heap = []
        for n in arr:
            heapq.heappush(heap,n)
        return heapq.heappop(heap)   

          
def main():
    user_input = input("Enter elements to insert in the heap (with space in between): ")
    arr = list(map(int, user_input.strip().split()))
    sol = Solution()
    result = sol.minHeap(arr)
    print(result)
if __name__ == "__main__":
    main()
import heapq
class Solution:
    def kSmallest(self, arr, k):
        heap = []
        for n in arr:
            heapq.heappush(heap, n)
        for _ in range(k-1):
            heapq.heappop(heap)
        return heapq.heappop(heap)      

          
def main():
    user_input = input("Enter elements of the array (with space in between): ")
    arr = list(map(int, user_input.strip().split()))
    k = int(input("Enter k: "))
    sol = Solution()
    result = sol.kSmallest(arr, k)
    print(result)
if __name__ == "__main__":
    main()
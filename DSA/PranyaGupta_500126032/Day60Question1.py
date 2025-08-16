import heapq
class Solution:
    def kSortedArray(self, arr, k):
        n = len(arr)
        res = []
        heap = arr[:k+1]
        heapq.heapify(heap)
        for i in range(k+1, n):
            res.append(heapq.heappop(heap))
            heapq.heappush(heap, arr[i])
        while heap:
            res.append(heapq.heappop(heap))
        return res    


def main():
    user_input = input("Enter the elements of heap (separated by space): ")
    arr = list(map(int, user_input.strip().split()))
    k = int(input("Enter k: "))
    sol = Solution()
    print(sol.kSortedArray(arr, k))

if __name__ == "__main__":
    main()                

                 


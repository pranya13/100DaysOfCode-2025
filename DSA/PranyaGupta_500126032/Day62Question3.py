import heapq

class Solution:
    def kthLargestSum(self, arr, k):
        n = len(arr)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + arr[i]

        min_heap = []
        for i in range(n):
            for j in range(i + 1, n + 1):
                curr_sum = prefix[j] - prefix[i]
                heapq.heappush(min_heap, curr_sum)
                if len(min_heap) > k:
                    heapq.heappop(min_heap)

        return min_heap[0]


def main():
    arr = list(map(int, input("Enter array elements: ").split()))
    k = int(input("Enter k: "))
    sol = Solution()
    print(sol.kthLargestSum(arr, k))


if __name__ == "__main__":
    main()

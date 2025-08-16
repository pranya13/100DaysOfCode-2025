import heapq

class Solution:
    def kClosest(self, arr, k, target):
        maxheap = []
        for n in arr:
            dist = abs(n-target)
            heapq.heappush(-dist, -n)
            if len(maxheap)>k:
                heapq.heappop(maxheap)
        res = [-n for (_, n) in maxheap]
        return res


def main():
    user_input = input("Enter the lengths of ropes (separated by space): ")
    arr = list(map(int, user_input.strip().split()))
    k = int(input("Enter k: "))
    target = int(input("Enter target: "))
    sol = Solution()
    result = sol.kClosest(arr, k, target)
    print("Minimum total cost to connect ropes:", result)


if __name__ == "__main__":
    main()

import heapq

class Solution:
    def mergeKSortedArrays(self, arr):
        heap = []
        for num in arr:
            for n in num:
                heapq.heappush(heap, n)
        res = []        
        while heap:
            res.append(heapq.heappop(heap))
        return res    
        


def main():
    k = int(input("Enter number of sorted arrays: "))
    arr = []
    for i in range(k):
        user_input = input(f"Enter sorted array {i+1} elements (space separated): ")
        arr.append(list(map(int, user_input.strip().split())))
    
    sol = Solution()
    res = sol.mergeKSortedArrays(arr)
    print(res)


if __name__ == "__main__":
    main()

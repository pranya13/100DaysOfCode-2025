import heapq
class Solution:
    def kLargest(self, arr, k):
        heap = arr[:k]
        heapq.heapify(heap)
        for n in arr[k:]:
            if n > heap[0]:
                heapq.heapreplace(heap, n)
        return sorted(heap, reverse=True)        


          
def main():
    user_input = input("Enter elements of the array (with space in between): ")
    arr = list(map(int, user_input.strip().split()))
    k = int(input("Enter k: "))
    sol = Solution()
    result = sol.kLargest(arr, k)
    print(result)
if __name__ == "__main__":
    main()
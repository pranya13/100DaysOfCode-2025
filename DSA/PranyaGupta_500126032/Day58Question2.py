import heapq
class Solution:
    def heapify(self, arr, n, i):
        hmax = i
        l = 2*i+1
        r = 2*i+2
        if l<n and arr[l]>arr[hmax]:
            hmax = l
        if r<n and arr[r]>arr[hmax]:
            hmax = r
        if hmax != i:
            arr[i], arr[hmax] = arr[hmax], arr[i] 
            self.heapify(arr, n, hmax)      
            

    def maxHeap(self, arr):
        n = len(arr)
        for i in range(n//2-1, -1, -1):
            self.heapify(arr, n, i)
        return arr    


          
def main():
    user_input = input("Enter elements of the array (with space in between): ")
    arr = list(map(int, user_input.strip().split()))
    sol = Solution()
    result = sol.maxHeap(arr)
    print(result)
if __name__ == "__main__":
    main()
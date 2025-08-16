import heapq
class Solution:
    def isMaxHeap(self, arr):
        n = len(arr)
        for i in range(n//2):
            l = 2*i+1
            r = 2*i+2
            if l<n and arr[i] <  arr[l]:
                return False
            if r<n and arr[i] < arr[r]:
                return False
        return True
               


          
def main():
    user_input = input("Enter elements of the array (with space in between): ")
    arr = list(map(int, user_input.strip().split()))
    sol = Solution()
    result = sol.isMaxHeap(arr)
    print(result)
if __name__ == "__main__":
    main()


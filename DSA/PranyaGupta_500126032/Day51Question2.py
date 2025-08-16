from collections import defaultdict
class Solution:
    def smallestSubarray(self, arr, x):
        l = 0
        minlen = float('inf')
        currsum = 0
        for r in range(len(arr)):
            currsum+=arr[r]
            while currsum>=x and l<=r:
                minlen = min(minlen, r-l+1)
                currsum-=arr[l] 
                l+=1
        return minlen if minlen!=float('inf') else 0         
                

def main():
    user_input = input("Enter elements of the array (with space in between): ")
    arr = list(map(int, user_input.strip().split()))
    x = int(input("Enter the sum: "))
    sol = Solution()
    result = sol.smallestSubarray(arr, x)
    print(result)
if __name__ == "__main__":
    main()
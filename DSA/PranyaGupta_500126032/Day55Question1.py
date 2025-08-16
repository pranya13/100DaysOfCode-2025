
class Solution:
    def longestSubarray(self, arr, k):
        l=0
        cs = 0
        maxlen = 0
        for r in range(len(arr)):
            cs+=arr[r]
            while cs>k:
                cs-=arr[l]
                l+=1
            if cs == k:
                maxlen = max(maxlen , r-l+1)

        return maxlen        

            





          
def main():
    user_input = input("Enter elements of the array (with space in between): ")
    k  = int(input("Enter k: "))
    arr = list(map(int, user_input.strip().split()))
    sol = Solution()
    result = sol.longestSubarray(arr, k)
    print(result)
if __name__ == "__main__":
    main()
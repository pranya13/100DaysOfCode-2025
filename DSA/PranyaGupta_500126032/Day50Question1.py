class Solution:
    def maxSumK(self, arr, k):
        i=0
        j= k+i
        n = len(arr)
        maxsum = 0
        currsum = sum(arr[i:j])
        while(j<n):
            currsum = currsum-arr[i]+arr[j]
            maxsum = max(maxsum, currsum)
            i+=1
            j=i+k
        return maxsum
def main():
    user_input = input("Enter elements of the array (with space in between): ")
    arr = list(map(int, user_input.strip().split()))
    k = int(input("Enter k: "))
    sol = Solution()
    result = sol.maxSumK(arr, k)
    print(result)
if __name__ == "__main__":
    main()
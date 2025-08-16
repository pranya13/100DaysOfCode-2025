
class Solution:
    def longestMountain(self, arr):
        n = len(arr)
        maxm = 0
        for i in range(1,n-1):
            if arr[i-1] < arr[i] > arr[i+1]:
                l = i-1
                r = i+1
                while l>0 and arr[l-1] <arr[l]:
                    l-=1
                while r<n-1 and arr[r+1]<arr[r]:
                    r+=1
                maxm = max(maxm, r-l+1)  
        return maxm                       
                

def main():
    user_input = input("Enter elements of the array (with space in between): ")
    arr = list(map(int, user_input.strip().split()))
    sol = Solution()
    result = sol.longestMountain(arr)
    print(result)
if __name__ == "__main__":
    main()
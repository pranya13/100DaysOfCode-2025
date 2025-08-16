
class Solution:
    def productLessThanK(self, arr, k):
        p = 1
        c= 0
        l = 0
        for r in range(len(arr)):
            p*=arr[r]
            while p>=k and l<=r:
                p//=arr[l]
                l+=1
            c+=(r-l+1)
        return c        


          
def main():
    user_input = input("Enter elements of the array (with space in between): ")
    k  = int(input("Enter k: "))
    arr = list(map(int, user_input.strip().split()))
    sol = Solution()
    result = sol.productLessThanK(arr, k)
    print(result)
if __name__ == "__main__":
    main()
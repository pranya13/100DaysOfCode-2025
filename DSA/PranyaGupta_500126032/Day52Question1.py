from collections import defaultdict
class Solution:
    def findPair(self, arr, x):
        arr.sort()
        l = 0
        r = len(arr)-1
        while(l!=r):
            currsum = arr[l]+arr[r]
            if currsum == x:
                return True
            elif currsum>x:
                r-=1
            elif currsum<x:
                l+=1 
        return False           
       

def main():
    user_input = input("Enter elements of the array (with space in between): ")
    arr = list(map(int, user_input.strip().split()))
    x = int(input("Enter the target sum: "))
    sol = Solution()
    result = sol.findPair(arr, x)
    print(result)
if __name__ == "__main__":
    main()
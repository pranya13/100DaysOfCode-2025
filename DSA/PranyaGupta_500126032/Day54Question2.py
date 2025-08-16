
class Solution:
    def maxWater(self, arr):
        l = 0
        r = len(arr) -1
        maxarea = 0
        area = 0
        while l<r:
            area = min(arr[l], arr[r])*(r-l)
            maxarea = max(maxarea, area)
            if arr[l] < arr[r]:
                l+=1
            else:
                r-=1
        return maxarea                              

          


def main():
    user_input = input("Enter elements of the array (with space in between): ")
    arr = list(map(int, user_input.strip().split()))
    sol = Solution()
    result = sol.maxWater(arr)
    print(result)
if __name__ == "__main__":
    main()
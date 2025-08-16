from collections import Counter
class Solution:
    def maxStreak(self, arr):
        ms = 0
        cs = 1
        curr = arr[0]
        i=1
        while i<len(arr):
            if arr[i] == curr:
                cs+=1
                ms = max(ms, cs)
            else:
                cs=0
                curr = arr[i]        
            i+=1
        return ms    


def main():
    user_input = input("Enter elements of the array (with space in between): ")
    arr = list(map(int, user_input.strip().split()))
    sol = Solution()
    result = sol.maxStreak(arr)
    print(result)
if __name__ == "__main__":
    main()
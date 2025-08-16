
class Solution:
    def BinarySubarray(self, arr, goal):
        ps = 0
        c = 0
        freq = {0:1}
        for n in arr:
            ps+=n
            num = ps-goal
            if num in freq:
                c+=freq[num]
            freq[ps] = freq.get(ps, 0)+1
        return c        


          
def main():
    user_input = input("Enter elements of the array (with space in between): ")
    arr = list(map(int, user_input.strip().split()))
    goal = int(input("Enter goal sum: "))
    sol = Solution()
    result = sol.BinarySubarray(arr, goal)
    print(result)
if __name__ == "__main__":
    main()
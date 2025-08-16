from collections import defaultdict
class Solution:
    def fruit(self, arr):
        l = 0
        maxlen = 0
        charc = defaultdict(int)
        for r in range(len(arr)):
            charc[arr[r]]+=1
            while len(charc)>2:
                charc[arr[l]]-=1
                if charc[arr[l]] ==0:
                    del charc[arr[l]]
                l+=1
        if len(charc) == 2:
            maxlen = max(maxlen, r-l+1)
        return maxlen   



                



def main():
    user_input = input("Enter elements of the array (with space in between): ")
    arr = list(map(int, user_input.strip().split()))
    sol = Solution()
    result = sol.fruit(arr)
    print(result)
if __name__ == "__main__":
    main()
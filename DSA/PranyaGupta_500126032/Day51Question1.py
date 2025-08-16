from collections import defaultdict
class Solution:
    def kUniqueString(self, s, k):
        l = 0
        maxlen = 0
        charc = defaultdict(int)
        for r in range(len(s)):
            charc[s[r]]+=1
            while len(charc)>k:
                charc[s[l]]-=1
                if charc[s[l]] ==0:
                    del charc[s[l]]
                l+=1
        if len(charc) == k:
            maxlen = max(maxlen, r-l+1)
        return maxlen                







def main():
    s = input("Enter the string: ")
    k = int(input("Enter the k: "))
    sol = Solution()
    result = sol.kUniqueString(s, k)
    print(result)
if __name__ == "__main__":
    main()
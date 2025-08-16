
class Solution:
    def longestSubstring(self, s):
        cs = set()
        l = 0
        maxlen = 0
        for r in range(len(s)):
            while s[r] in cs:
                cs.remove(s[l])
                l+=1
            cs.add(s[r])   
            maxlen = max(maxlen, r-l+1)
        return maxlen            

          
def main():
    s  = input("Enter the string: ")
    sol = Solution()
    result = sol.longestSubstring(s)
    print(result)
if __name__ == "__main__":
    main()
class Solution:
    def noOfanagram(self, s, p):
        sl = len(s)
        pl = len(p)
        i=0
        j=i+pl
        res = 0
        while j<=sl:
            if sorted(list(s[i:j])) == sorted(list(p)):
                res+=1
            i+=1
            j=i+pl
        return res        

def main():
    s = input("Enter the string: ")
    p = input("Enter the pattern: ")
    sol = Solution()
    result = sol.noOfanagram(s, p)
    print(result)
if __name__ == "__main__":
    main()
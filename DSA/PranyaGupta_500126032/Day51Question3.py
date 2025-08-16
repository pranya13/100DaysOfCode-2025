from collections import Counter
class Solution:
    def substr(self, s, t):
        tc = Counter(t)
        tn = len(tc)
        c = {}
        f = 0
        l =0
        minlen = float('inf')
        strt = 0
        for r, ch in enumerate(s):
            c[ch] = c.get(ch,0)+1
            if ch in tc and c[ch] ==tc[ch]:
                f+=1
            while f==tn:
                if r-l+1<minlen:
                    minlen = r-l+1
                    strt = l
                lc = s[l]
                c[lc]-=1
                if lc in tc and c[lc]< tc[lc]:
                    f-=1
                l+=1
        return "" if minlen==float('inf') else s[strt: strt+minlen]           

def main():
    s = input("Enter the string: ")
    t = (input("Enter the characters: "))
    sol = Solution()
    result = sol.substr(s, t)
    print(result)
if __name__ == "__main__":
    main()
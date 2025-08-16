
class Solution:
    def tappingRain(self, h):
        n = len(h)
        if n<3: return 0
        l = 0
        r = n-1
        lmax = 0
        rmax = 0
        wt = 0
        while l<=r:
            if h[l]<=h[r]:
                if h[l]>=lmax:
                    lmax = h[l]
                else:
                    wt += lmax- h[l]
                l+=1
            else:
                if h[r] >=rmax:
                    rmax = h[r]
                else:
                    wt+= rmax-h[r]
                r-=1
        return wt                        


                

def main():
    user_input = input("Enter the heights (with space in between): ")
    h = list(map(int, user_input.strip().split()))
    sol = Solution()
    result = sol.tappingRain(h)
    print(result)
if __name__ == "__main__":
    main()
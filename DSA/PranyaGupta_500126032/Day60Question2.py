import heapq
class Solution:
    def Median(self, arr):
        s = []
        l = []
        m = []
        for n in arr:
            heapq.heappush(s, -n)

            if s and l and (-s[0]>l[0]):
                val = -heapq.heappop(s)
                heapq.heappush(l, val)
            if len(s) > len(l)+1:
                val = -heapq.heappop(s)
                heapq.heappush(l, val)
            elif len(l) > len(s):
                val = heapq.heappop(l)
                heapq.heappush(s, -val) 
            if len(s) ==  len(l):
                med = (-s[0]+l[0])/2.0
            else:
                med = -s[0]
            m.append(med)
        return m                   


def main():
    user_input = input("Enter the elements of heap (separated by space): ")
    arr = list(map(int, user_input.strip().split()))
    sol = Solution()
    print(sol.Median(arr))

if __name__ == "__main__":
    main()                

                 


from collections import Counter
class Solution:
    def DiffPairs(self, arr, diff):
        res = []
        freq = Counter(arr)
        for n in arr:
            tp =()
            if freq[n+diff] >0:
                tp = (n, n+diff)
                res.append(tp)
        return res        

                  
       

def main():
    user_input = input("Enter elements of the array (with space in between): ")
    arr = list(map(int, user_input.strip().split()))
    diff = int(input("Enter the difference: "))
    sol = Solution()
    result = sol.DiffPairs(arr, diff)
    print(result)
if __name__ == "__main__":
    main()
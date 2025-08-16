
class Solution:
    def ThreeSum(self, arr):
        arr.sort()
        res = []
        for i in range(len(arr)-2):
            if i>0 and arr[i] == arr[i-1]:
                continue
            l = i+1
            r = len(arr)-1
            while l<r:
                s = arr[i]+arr[l]+arr[r]
                if s == 0:
                    res.append([arr[i], arr[l], arr[r]])
                    while l<r and arr[l] == arr[l+1]:
                        l+=1
                    while l<r and arr[r] == arr[r-1]:
                        r-=1
                    l+=1
                    r-=1        
                elif s>0:
                    r-=1
                else:
                    l+=1
        return res                    

          


def main():
    user_input = input("Enter elements of the array (with space in between): ")
    arr = list(map(int, user_input.strip().split()))
    sol = Solution()
    result = sol.ThreeSum(arr)
    print(result)
if __name__ == "__main__":
    main()
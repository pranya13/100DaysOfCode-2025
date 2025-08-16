class Solution:
    def targetSum(self, arr, target):
        i=0
        j=i+1
        n = len(arr)
        s=0
        while j<=n:
            s = sum(arr[i:j])
            if s==target:
                return f"Target sum found at index {i} to {j-1}"
            elif s < target:
                j+=1
            else:
                i+=1
                if i==j:
                    j+=1
        return -1            




        
def main():
    user_input = input("Enter elements of the array (with space in between): ")
    arr = list(map(int, user_input.strip().split()))
    target = int(input("Enter the target sum: "))
    sol = Solution()
    result = sol.targetSum(arr, target)
    print(result)
if __name__ == "__main__":
    main()

class Solution:
    def heapify(self, arr, n, i):
        lmax = i
        l = 2*i+1
        r = 2*i+2
        if arr[l]> arr[lmax] and l<n:
            lmax = l
        
        if arr[r]> arr[lmax] and r<n:
            lmax = r

        if lmax!=i:
            arr[i], arr[lmax] = arr[lmax], arr[i]
            self.heapify(arr, n , lmax)


    def HeapSort(self, arr):
        n = len(arr)
        for i in range(n//2-1, -1, -1):
            self.heapify(arr, n, i)
        for i in range(n-1, 0 , -1):
            arr[i], arr[0] = arr[0], arr[i]
            self.heapify(arr, i, 0)
        return arr                   


def main():
    user_input = input("Enter the elements of min heap (separated by space): ")
    arr = list(map(int, user_input.strip().split()))
    sol = Solution()
    print(sol.HeapSort(arr))

if __name__ == "__main__":
    main()                

                 


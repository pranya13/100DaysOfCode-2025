import heapq
class Solution:
    def MaxHeap(self, arr):
        maxheap=[-n for n in arr]
        heapq.heapify(maxheap)
        return [-n for n in maxheap]                    


def main():
    user_input = input("Enter the elements of min heap (separated by space): ")
    arr = list(map(int, user_input.strip().split()))
    sol = Solution()
    print(sol.MaxHeap(arr))

if __name__ == "__main__":
    main()                

                 


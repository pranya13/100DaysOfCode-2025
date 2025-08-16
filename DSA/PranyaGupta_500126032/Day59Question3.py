import heapq
class Solution:
    def buildHeap(self, arr):
        ac = arr.copy()
        heapq.heapify(ac)
        return ac 
    def HeapIdentical(self, arr1, arr2):
        h1 = self.buildHeap(arr1)
        h2 = self.buildHeap(arr2)
        if len(h1) != len(h2):
            return False
        for i in range(len(h1)):
            if h1[i] != h2[i]:
                return False
        return True    




def main():
    user_input1 = input("Enter the elements of heap1 (separated by space): ")
    arr1 = list(map(int, user_input1.strip().split()))
    user_input2 = input("Enter the elements of heap2 (separated by space): ")
    arr2 = list(map(int, user_input2.strip().split()))
    sol = Solution()
    print(sol.HeapIdentical(arr1, arr2))

if __name__ == "__main__":
    main()                

                 


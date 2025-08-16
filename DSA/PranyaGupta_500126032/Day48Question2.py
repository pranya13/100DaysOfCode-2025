class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self, data):
        self.queue.append(data)
    def dequeue(self):
        if not self.isEmpty():
            return self.queue.pop(0)
        else:
            return None
    def qsize(self):
        return len(self.queue)
    def isEmpty(self):
        return len(self.queue)==0
    def printQueue(self):
        print(self.queue)
    
    

class Solution():
    def Unique(self, q):
        s = set()
        for i in range(q.qsize()):
            val = q.dequeue()
            if val in s:
                return False
            s.add(val)
        return True      
               

def main():
    user_input = input("Enter the elements of Queue (with space in between): ")
    arr = list(map(int, user_input.strip().split()))
    q = Queue()
    for n in arr:
        q.enqueue(n)
    sol = Solution()
    print(sol.Unique(q))


if __name__ == "__main__":
    main()  
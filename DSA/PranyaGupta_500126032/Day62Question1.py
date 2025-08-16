import heapq

class Solution:
    def minCostRopes(self, arr):
        heapq.heapify(arr)
        total_cost = 0

        while len(arr) > 1:
            first = heapq.heappop(arr)
            second = heapq.heappop(arr)

            cost = first + second
            total_cost += cost

            heapq.heappush(arr, cost)

        return total_cost


def main():
    user_input = input("Enter the lengths of ropes (separated by space): ")
    arr = list(map(int, user_input.strip().split()))
    sol = Solution()
    result = sol.minCostRopes(arr)
    print("Minimum total cost to connect ropes:", result)


if __name__ == "__main__":
    main()

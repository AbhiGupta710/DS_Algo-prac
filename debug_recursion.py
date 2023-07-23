class Solution:
    def maxProfit(self, prices) -> int:

        left, right = 0, len(prices) - 1
        buy, sell = 0, len(prices) - 1

        for i in range(len(prices)):
            print(buy, sell, '====', left, right)

            if (prices[right] > prices[sell]) and (right > buy):
                print('upd sell')
                sell = right

            if (prices[left] < prices[buy]) and (left < sell):
                print('upd', 'buy')
                buy = left

            left += 1
            right -= 1
        print(prices[sell], prices[buy])
        if (prices[sell] - prices[buy]) > 0:
            return prices[sell] - prices[buy]
        return 0


obj = Solution()
print(obj.maxProfit([1, 4, 2]), 'ans')
print(obj.maxProfit([3, 2, 6, 5, 0, 3]), 'ans')

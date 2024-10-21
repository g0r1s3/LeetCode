class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewel_count = 0
        for jewel in jewels:
            for stone in stones:
                if jewel == stone:
                    jewel_count += 1
        return jewel_count

solution = Solution()
print(solution.numJewelsInStones("aA", "aAAbbbb"))
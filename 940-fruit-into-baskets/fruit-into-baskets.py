class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l = 0
        fruit_cnt = Counter()
        total_fruit = 0
        for r in range(len(fruits)):
            fruit_cnt[fruits[r]] += 1
            while len(fruit_cnt) > 2:
                fruit_cnt[fruits[l]] -= 1
                if fruit_cnt[fruits[l]] == 0:
                    fruit_cnt.pop(fruits[l])
                l += 1
            total_fruit = max(total_fruit, r - l + 1)
        return total_fruit


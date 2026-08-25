class Solution:
    def twoSum(self, numbers: list, target: int) -> list:
        i = 0
        j = len(numbers)-1

        while numbers[i] + numbers[j] != target:            
            if numbers[j] + numbers[i] < target or i == j:
                j = len(numbers) - 1
                i += 1
                continue

            if numbers[i] + numbers[j] > target:
                j -= 1
                continue

        return [i+1, j+1]
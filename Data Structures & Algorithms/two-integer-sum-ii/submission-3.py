class Solution:
    def twoSum(self, numbers: list, target: int) -> list:
        n = len(numbers)

        remainder = target
        i = 0
        j = n-1

        while True:
            if remainder == target:
                remainder -= numbers[i]
            
            if i == n-1:
                break
            
            if remainder - numbers[j] == 0:
                break

            if remainder > numbers[j] or i == j:
                j = n - 1
                i += 1
                remainder = target
                continue

            if remainder < numbers[j]:
                j -= 1
                continue

        return [i+1, j+1]
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        result = 0

        ldividend = abs(dividend)
        ldivisor = abs(divisor)

        while ldividend >= ldivisor:
            num_shifts = 0
            while (ldivisor << num_shifts) <= ldividend:
                num_shifts += 1
            num_shifts -= 1
            result += 1 << num_shifts
            ldividend -= ldivisor << num_shifts

        if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
            result = -result

        return result
        # time complexity is(O(log(2n))) , one logn for each while loop
        # space complexity is O(1)

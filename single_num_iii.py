class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # time complexity is O(n), space complexity of O(1)

        # 1) find xor of all numbers, since result will be the xor of two numbers that do not have duplicares
        xor_result = 0

        for num in nums:
            xor_result ^= num

        rightmost_set_bit = 1
        # 2) find rightmost set bit by & ing the xor result of all the numbers and the rightmost_set_bit we assumed to be 1 and checking if this gives you a zero , if it does keep moving until the rightmost_set_bit is not zero and then the right most place that gives you a non-zero digit is the rightmost set by english and logic
        while (xor_result & rightmost_set_bit) == 0:
            rightmost_set_bit <<= 1

        x = y = 0
        # x stores the XOR of group1 and y stores the XOR of group2 which is what is returned since XOR operation eliminates or makes repeated numbers 0
        group1 = []
        group2 = []  # holds all the numbers which give an

        for num in nums:
            # if the binary number returned by the AND operation is 1, then x is XOR with the num in the list of nums input and then the same x is used later on meaning if repeated numbers come, at some point of the x continual usage, it becomes 0 indicating that the
            if num & rightmost_set_bit:  # obtained by left shift calculation above
                x ^= num
                group1.append(num)

            else:
                y ^= num
                group2.append(num)

        return [x, y]

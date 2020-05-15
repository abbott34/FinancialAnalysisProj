'''
https://www.youtube.com/watch?v=9Q73ScVu2GI
Above is the link to the question. Stop watching the video at 3:30, that is as much as you need to know. If you watch
more then I think he gives away the solution but idk, I haven't watched that far lol.

Row a is the top half of the domino while row b is the bottom half. Your goal is to make one row all the same number.
What is the minimum number of "flips" of a domino such that either row a or row b has the same number across?
If it is impossible for every element of a or b to have the same number then return -1
'''

# Example input and output
# Input:
a = [1, 5, 2, 1, 1]
b = [2, 1, 1, 4, 2]
# Output:
ans = 2


# Implementation 1
def min_filps(a, b):
    # First I'm just going to find the most common number on a half of a domino
    keys = [1, 2, 3, 4, 5, 6]
    dict_keys_a = {k: 0 for k in keys}
    dict_keys_b = {k: 0 for k in keys}
    for i in range(len(a)):
        dict_keys_a[i+1] += 1
        dict_keys_a[i + 1] += 1


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        num = 0
        neg_flag = False
        if x < 0:
            neg_flag = True
        while x != 0:
            num *= 10
            num += x % 10
            x /= 10
        if neg_flag:
            return num * -1
        return num
a = Solution()
print(a.reverse(321))

while !(1 < 5):

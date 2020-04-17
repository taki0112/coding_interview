from collections import Counter
class Solution:
    def countBits(self, num):
        x = []
        for i in range(num+1):
            binary_num = format(i, 'b')
            binary_dict = Counter(binary_num)
            one_num = binary_dict['1']

            x.append(one_num)

        return x
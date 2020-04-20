class Solution:
    def countSubstrings(self, s: str) -> int:
        s_len = len(s)
        p_num = 0

        for i in range(s_len):
            for j in range(i, s_len):
                split_s = s[i:j + 1]
                if self.check_palindromic(split_s):
                    p_num += 1

        return p_num

    def check_palindromic(self, s):
        if s == s[::-1]:
            return True
        else:
            return False

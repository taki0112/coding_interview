class Solution:
    def dailyTemperatures(self, T):
        x, stack = [0] * len(T), []
        for i in range(len(T)):
            while stack and T[stack[-1]] < T[i]:
                x[stack.pop()] = i - stack[-1]
            stack.append(i)
        return x
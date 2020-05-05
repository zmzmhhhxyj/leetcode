def dailyTemperatures(T):
    ans = [0] * len(T)
    stack = []
    for i, t in enumerate(T):
        while stack and T[stack[-1]] < t:
            cur = stack.pop()
            ans[cur] = i - cur
        stack.append(i)

    return ans

ans = dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])
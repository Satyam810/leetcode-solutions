        ans = []
        for u, v in queries:
            a, b = get_i[u], get_i[v]
            if a > b: a, b = b, a
            if a == b: ans.append(0); continue

            curr, steps = a, 0
            for j in range(LOG - 1, -1, -1):
                if st[curr][j] < b:
                    curr = st[curr][j]
                    steps += (1 << j)

            ans.append(steps + 1 if st[curr][0] >= b else -1)

        return ans

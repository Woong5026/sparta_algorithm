n = int(input()) # 초기값
cost_per_home = [] # 값을 넣을 배열값

for _ in range(n):
    cost_per_home.append(list(map(int, input().split())))

    dp = [cost_per_home[0]]

for i in range(1,n):
    cost_per_color = []

    red = min(dp[i-1][1], dp[i-1][2])
    cost_per_color.append(red + cost_per_home[i][0])

    green = min(dp[i-1][0], dp[i-1][2])
    cost_per_color.append(green + cost_per_home[i][1])

    blue = min(dp[i-1][0], dp[i-1][1])
    cost_per_color.append(blue + cost_per_home[i][2])

    dp.append(cost_per_color)

print(min(dp[n-1]))


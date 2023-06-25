# 讀取檔案的過程中，求讀取進度

data = []

with open('review.txt', 'r') as f:
    for line in f:
        data.append(line)
        print(len(data))  # 一個一個印出現在讀到第幾個留言


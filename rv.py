# review.txt為Amazon網站上其中的一百萬筆留言檔

data = []

with open('review.txt', 'r') as f:
    for line in f:
        data.append(line)

print(len(data))
print(data[0]) # 第一個留言
print(data[1]) # 第二個留言


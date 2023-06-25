# 讀取檔案的過程中，求讀取進度(每1000筆報一次進度)

data = []

i = 0

with open('review.txt', 'r') as f:
    
    for line in f:
        data.append(line)

        i = i + 1  # i += 1

        if i % 1000 == 0:
            print(len(data)) 

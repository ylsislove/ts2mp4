import os
import re

result = []

# 获取所有存放视频的文件夹
a = os.listdir(".")
a = [i for i in a if len(i.split('_')) > 2]

# 按文件夹后缀数字大小排序
a.sort(key=lambda l: int(re.findall('\d+', l)[-1]), reverse=False)
# print(a)

# 遍历所有视频文件
for i in a:
    b = i.split('_')
    for j in range(int(b[1]), int(b[2])+1):
        subfile = os.path.join(i, f'{j}.ts')
        # 判断该视频文件是否存在
        if os.path.isfile(subfile):
            result.append(f"file '{subfile}'")

# print(result)

# 生成txt文件
with open('result.txt', 'w') as f:
    for i in result:
        f.writelines(i)
        f.writelines('\n')

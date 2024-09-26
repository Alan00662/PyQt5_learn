# 错误的代码示例
file = None
try:
    file = open('test.txt', 'r')
    content = file.read()
except IOError as e:
    print(e)
finally:
    if file is not None:
        file.close()
 
# 修正后的代码示例
try:
    with open('test.txt', 'r') as file:
        content = file.read()
except IOError as e:
    print(e)
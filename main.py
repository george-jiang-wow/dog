import requests
#从https://wedog.ru/words获得文本
r = requests.get('https://wedog.ru/words').text
# 以 "content":"分割字符串
t = r.split('content":"')
# 去掉第一个字符串
t.pop(0)
# 以","lickCount"分割字符串
ans=(t[0].split('","lickCount'))[0]
#输出
print(ans)

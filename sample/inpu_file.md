## 这是我的markdown说明
```
s = ""
while True:
    v1 = input("username")
    v2 = input("password")
    v3 = input("email")
    test = '{0}\t{1}\t{2}\n'
    v = test.format(v1,v2,v3)
    s = s + v
    temp = input('请输入指令：')
    temp1 = temp.upper()
    if temp == 'Q' or temp == 'q':
        break
    else:
        pass
print(s.expandtabs(20))
```
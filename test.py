s = input()
k = int(input())
l = len(s)
dic = {}
vowel = ['a','e','i','o','u']
# print(l)
for i in range(l-k):
    new = s[i:i+k]
    c = 0
    for j in new:
        if j in vowel:
            c = c+1
    if c != dic.keys():
        dic[c] = ''.join(new)
    else:
        continue
mx = max(dic, key=dic.get)
print(dic)
print(dic[mx])

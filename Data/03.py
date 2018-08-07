#! coding: euc-jp
str='Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics'
ans=[]
words=str.split(' ')
for word in words:
  count=0
  for char in word:
    if char.isalpha():
      count+=1
  ans.append(count)
print(ans)

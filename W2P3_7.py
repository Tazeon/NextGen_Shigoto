word = str(input())
bigcnt = 0
smallcnt = 0
for i in range(len(word)):
  if word[i].isupper():
    bigcnt += 1
  elif word[i].islower():
    smallcnt += 1
print(smallcnt)
print(bigcnt)
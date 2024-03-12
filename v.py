s=input()
a="aeiouAEIOU"
count=0
count1=0
for i in range(len(s)):
  if(i%2==0):
    if s[i] in a:
      count+=1
  else:
    if s[i] in a:
      count1+=1
print(count)
print(count1)
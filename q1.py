def reverse(s):
  str=" "
  for i in s:
  str=i+str
return str
s=input()
print("original string: ")
print(s)
print("reversed string: ")
print(reverse(s))

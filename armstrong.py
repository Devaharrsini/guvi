n = int(input())
r = int(input())

for i in range(n,r):
  t=i
  a=0
  
  while i>0:
    a = a + ((i%10)**3)
    i = i//10
  if t == a:
    print(a)

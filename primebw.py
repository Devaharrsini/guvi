intlist = list()
n = int(input())
r = int(input())

for i in range(n,r):
  if i>1:
    for j in range(2,i):
      if i%j == 0:
        break
    else:
      print(i)

num=int(input())
sum=0
while(num!=0):
  x=num%10
  sum=(sum*10)*x
  num=num//10
  print(x,end=' ')

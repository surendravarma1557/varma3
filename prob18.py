lower = int(input())
upper = int(input())

for n in range(lower,upper):
   sum = 0
   temp = n
   while temp > 0:
       digit = temp % 10
       sum += digit ** 3
       temp //= 10

   if n == sum:
       print(n)

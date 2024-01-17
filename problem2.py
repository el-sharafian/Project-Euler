sum = 0
i = 1
j = 1
s=0

def even(num):
    if(num%2 == 0):
        return True
    else:
        return False 
        

while (s < 4000000):
    s=i+j
    i=j
    j=s
    if(even(s)):
        sum=sum+s

print('sum of even numbers:', sum)
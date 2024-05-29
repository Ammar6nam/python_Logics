
# print (random.random())
# print(random.randint(1,6))
# a=bool(random)
# b=True

# if a and b:
#     print ('Both A and B are True.')

c:int=10
d:int=100
# if c>=10 and d<=1000:
#     print('Both conditions are satisfied!')
# else:
#     print('One or both conditions were not met' )

# if c==0 or d==100:
#     print('Both or one are Truthy values')
# else:
#     print('Both are NOT Truthy values' )

# n=None
# m={}

# if m:
#     print('The value of n is : ',n)
# else:
#     print('The N is set to None: ',n)

# x=input('Type your username: ') or 'Unknown'
# print(x)

import random
a=0
b=0
while(a<0.9 or (b<10 and isOdd(b))):
    b+=1
    a=random.random()
print(b)
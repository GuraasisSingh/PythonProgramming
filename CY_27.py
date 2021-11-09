import random
'''
#random.seed(10)#initialise random number generator
#print(random.random())
#random.seed(3)#initialise random number generator
print(random.random())
state=random.getstate()
#print(random.random())
#print(state)
random.setstate(state)
print(random.random())
'''
print(random.randint(3,8))
s=["apple","cherry","guava"]
#print(random.choice(s))
#print(random.choices(s))
#print(random.choices(s,weights=[5,1,1],k=2))
random.shuffle(s)
print(s)
print(random.random())#0.0 to 1.0

import random
x=int(20*random.random()+1)
z=0
while z != x:
    z=int(input("Shoot!: "))
    if z > x:
        print("Too large!")
    elif z < x:
        print("Too small!")
else:
    print("Perfectly!")

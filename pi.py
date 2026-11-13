import numpy as np
import random

# pi
pi=np.pi

# Retrieves the number of slices and points desired by user
while True:
    try:
        slices=int(input('\nHow many slices would you like to have on the interval between -1 and 1?  '))
        number=int(input('How many points would you like to plot on this interval?  '))
        if slices==int(slices) and number==int(number):
            break
        else:
            pass
    except ValueError:
        pass

# Slices the interval according to user input
points=np.linspace(-1,1,slices+2)

# Randomly chooses points in the specified region
x,y=[],[]
for i in range(number):
    x.append(random.choice(points))
    y.append(random.choice(points))

# Calculates the distance of the points from the Origin
modulus=[]
for i in range(number):
    modulus.append(x[i]**2+y[i]**2)

# Checks whether or not a point is in the unit circle
tally=[]
for i in modulus:
    if float(random.choice(modulus))<=1:
        tally.append(1)
    else:
        tally.append(0)

# Approximates pi based on the number of points in the unit circle
pi_approx=4*sum(tally)/len(tally)

# Calculates the error in the approximation
error=100*abs(pi-pi_approx)/pi
error=round(error,4)

print(f'\nValue of pi: {pi}')
print(f'Approximation: {pi_approx}')
print(f'Error: {error}%\n')

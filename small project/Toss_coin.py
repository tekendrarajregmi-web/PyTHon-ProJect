#Tossing a coin
import numpy as ny
import random as ra

"""
#In fair coin
0 = Tail
1 = Head
"""
coin = ny.array([1,0])

select = ra.choice(coin)

if 0 == select:
    result = "Tail"
elif 1 == select:
    result = "Head"
  
print(f"Output: {result}")

#calculating similarity with help of cosQ
import numpy as ny

a = ny.array([0.20,0.80])
b = ny.array([0.45,0.65])

cosQ = ny.dot(a,b)/ny.linalg.norm(a)*ny.linalg.norm(b)

print(f"similarity bwtween a & b: {cosQ * 100:.4f}")

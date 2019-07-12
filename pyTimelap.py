import time
s = time.time()

for i in range(10000):
    for j in range(10000):
        i=i+1

e = time.time()
print(e-s)

# 

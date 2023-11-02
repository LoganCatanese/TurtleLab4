import matplotlib.pyplot as plt
#import numpy as np

fig, ax = plt.subplots() 
loopVal = 4

aX = int(input())
aB = int(input())
aC = int(input())
aD = int(input())
#ax.plot([aX,aB,aC,aD], [aX,aB, aC, aD])
for i in range (loopVal):
    aX += 4
    print(aX)
if aX > 100:
    print("VALUE IS OUT OF RANGE")
ax.plot([aX, aB, aC, aD], [10,11, 12, 14], linestyle='--', marker='o', color='b', label='line with marker')
plt.figure
plt.legend(loc='best')
plt.show()
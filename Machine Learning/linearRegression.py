from scipy import stats
import numpy as np
from matplotlib import pyplot as plt

#training data - size of house
x =np.array([112,345,198,305,372,550,302,470,578])
y =np.array([1000,1523,2103,2230,2600,3200,3409,3689,4460])

slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)

#scatter plot-Can be commented
plt.plot(x,y,'ro',color="black")

plt.ylabel('Price')
plt.xlabel('Size of House')
plt.axis([0,600,0,5000])

#plot a line
plt.plot(x,x*slope+intercept,'b')

plt.plot()
plt.show()

#Prediction
newX = 150
newY = newX*slope + intercept
print(newY)


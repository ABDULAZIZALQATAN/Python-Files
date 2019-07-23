import matplotlib.pyplot as plt

cValues = [0.0 , 0.2 , 0.4 , 0.6 , 0.8 , 1.0]
mapValues = [0.2274 , 0.0557 , 0.1369 , 0.1647 , 0.1751 , 0.1824]
plt.plot(cValues,mapValues)
plt.ylabel ("MAP Values")
plt.xlabel ("C Values")
plt.title("PorterStem - PL2")


plt.show()
print('Done')
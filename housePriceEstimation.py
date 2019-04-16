import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import time

startTime = time.time()

data = pd.read_csv("housePriceDataset.csv")

x = data["squareMeter"]
y = data["price"]
x = np.array(x)
y = np.array(y)

a, b, c, d = np.polyfit(x, y, 3)
z = np.arange(150)
plt.scatter(x, y)
plt.plot(z, a*(z**3) + b*(z**2) + c*z + d)
plt.show()

pause1Time = time.time()
m2Guess = float(input("Please, enter square meter m2?"))
continue1Time = time.time()
housePriceGuess = a*(m2Guess**3) + b*(m2Guess**2) + c*m2Guess + d
print("House Price Guess => $" + str(housePriceGuess))
pause2Time = time.time()
housePrice = float(input("Please, enter house price $?"))
continue2Time = time.time()
for i in np.arange(0, 1000, 0.001):
    guessPrice = a*(i**3) + b*(i**2) + c*i + d
    if(guessPrice < housePrice):
        continue
    else:
        print("Square Meter (m2) Guess => " + str(i) + "m2")
        break

print("{} Seconds".format((time.time() - continue2Time) + (pause2Time - continue1Time) + (pause1Time - startTime)))


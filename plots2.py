import math
import matplotlib.pyplot as plt


X1 = []
Y1 = []

X2 = []
Y2 = []

X3 = []
Y3 = []

sum2 = - math.log(2, math.e) * math.sqrt(3)
sum3 = 0

pi = 3.14159265358979

for i in range(0, 101):
    X1.append(i)
    Y1.append(0)

    X2.append(i)


    sum2 = sum2 + 3 * math.sqrt(3) * ((-1) ** i) / (3 * i + 1)
    Y2.append(abs(pi - sum2))


    X3.append(i)
    
    sum3 = sum3 + 4 * ((-1) ** i) / (2 * i + 1)
    Y3.append(abs(pi - sum3))




fig = plt.figure()

plot = fig.add_subplot(111)

plot.scatter(
    x=X1,
    y=Y1,
)

plot.scatter(
    x=X2,
    y=Y2,
    label="Hard"
)

plot.scatter(
    x=X3,
    y=Y3,
    label="easy"
)


plt.legend()


plt.show()


# root 3 = math.sqrt(3)
# 
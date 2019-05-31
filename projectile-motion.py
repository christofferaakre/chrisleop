import math
import matplotlib.pyplot as plt

def is_number(x):
    try:
        float(x)
        return True
    except ValueError:
        return False

def degrees_to_radians(theta):
    return theta * math.pi / 180
def radians_to_degrees(theta):
    return theta * 180 / math.pi

v = 11.9
theta = 52.03
m = 0.0026
vt = 5.65
g = 9.80665
k1 = m * g / vt
k2 = m * g / (vt ** 2)

time_step = 0.001

print(f"Initial velocity? Default = {v}")
res = input()
if is_number(res):
    v  = float(res)

print(f"Angle to the horizontal? Default = {theta}°")
res = input()
if is_number(res):
    v  = float(res)



def a_x(velocity):
    return 0
def a_y(velocity):
    return -g

def a2_x(velocity):
    return -k1 * velocity / m
def a2_y(velocity):
    return -k1 * velocity / m - g

def a3_x(velocity):
    return -math.copysign(k1 * (velocity ** 2) / m, velocity)
def a3_y(velocity):
    return -math.copysign(k1 * (velocity ** 2) / m, velocity) - g

theta = degrees_to_radians(theta)

X = []
Y = []

X2 = []
Y2 = []

X3 = []
Y3 = []

T = []

v_x = v * math.cos(theta)
v_y = v * math.sin(theta)

v_2x = v * math.cos(theta)
v_2y = v * math.sin(theta)

v_3x = v * math.cos(theta)
v_3y = v * math.sin(theta)

x = 0
y = 0

x2 = 0
y2 = 0

x3 = 0
y3 = 0


i = 0

motion = {
    "No air resistance": True,
    "Linear air resistance": True,
    "Quadratic air resistance": True
}

print("Launching projectiles")
while True in motion.values():
    i+= 1
    if y >= 0:
        X.append(x)
        Y.append(y)

        v_x += time_step * a_x(v_x)
        v_y += time_step * a_y(v_y)

        x += time_step * v_x
        y += time_step * v_y
    elif motion["No air resistance"]:
        print("Particle without air resistance has landed")
        motion["No air resistance"] = False
    if y2 >= 0:
        X2.append(x2)
        Y2.append(y2)


        v_2x += time_step * a2_x(v_2x)
        v_2y += time_step * a2_y(v_2y)

        x2 += time_step * v_2x
        y2 += time_step * v_2y

    elif motion["Linear air resistance"]:
        print("Particle with linear air resistance has landed")
        motion["Linear air resistance"] = False
    
    if y3 >= 0:
        X3.append(x3)
        Y3.append(y3)

        v_3x += time_step * a3_x(v_3x)
        v_3y += time_step * a3_y(v_3y)

        x3 += time_step * v_3x
        y3 += time_step * v_3y
    elif motion["Quadratic air resistance"]:
        print("Particle with quadratic air resistance has landed")
        motion["Quadratic air resistance"] = False


print(f"All particles have landed after {i} cycles of the while loop")


print("Creating layout...")
fig = plt.figure()
plot = fig.add_subplot(111)

plot.set_title(f'Projectile motion. v = {round(v, 2)}m/s, θ = {round(radians_to_degrees(theta), 2)}°')
plot.set_xlabel('Horizontal displacement (m)')
plot.set_ylabel('Vertical displacement (m)')




print("Scattering...")
plot.scatter(
    x=X,
    y=Y,
    s=3,
    label="No air resistance"
)

plot.scatter(
    x=X2,
    y=Y2,
    s=3,
    label="Linear air resistances"
)

plot.scatter(
    x=X3,
    y=Y3,
    s=3,
    label="Quadratic air resistance"
)


print("Showing plot...")
plt.show()

exit()
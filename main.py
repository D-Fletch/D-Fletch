# Temp converter problem (1)

def FtoC(F):
  return (F / 1.8) - 32

def CtoF(C):
  return (C * 1.8) + 32

C = 30
F = CtoF(C)

print(str(C), "degrees C is", str(F), "degrees F")

# characters problem (1)
a = "0123456789"
b = "abcdABCD@#!£"
print(a)
print(b)
print(a, b)

# fish tank volume problem (2)
def volume(length, depth, height):
  answer = (length * depth * height) / 1000
  print(answer, "litres")

length = float(input("Enter length: "))
dep = float(input("Enter depth: "))
height = float(input("Enter height: "))

volume(length, dep, height)

# microscopy problem (2)
mag = 4E-2 / 80E-6
print(round(mag), "times magnification")
# round function rounds to 500

# carpet cost problem (2)
def cost(width, length, price):
  size = width * length
  grippers = (width * 2) + (length * 2)
  underlay = size * 3
  total = (size * price) + 50 + grippers + underlay
  print("£", str(total))

wid = float(input("Enter width: "))
leng = float(input("Enter length: "))
price_a_meter = float(input("Enter price per meter: "))
cost(wid, leng, price_a_meter)

# energy bill calculator (3)
def bill(prev_reading, current_reading, calorific_value):
  kWh = (current_reading - prev_reading) * 1.022 * calorific_value / 3.6
  print("total bill=", str(kWh))

past_reading = float(input("Enter previous reading: "))
current = float(input("Enter current reading: "))
c_v = 39.3

bill(past_reading, current, c_v)

# circle properties problem (3)
def circle_time(diameter, arc_angle):
  radius = diameter / 2
  area = 3.14 * (radius ** 2)
  circumference = 3.14 * diameter
  arc_length = (circumference * arc_angle) / 360
  print("The radius is: ", radius)
  print("The area is: ", area)
  print("The circumference is: ", circumference)
  print("The arc length is: ", arc_length)

diameter = float(input("Enter diameter: "))
arc = float(input("Enter arc length: "))

circle_time(diameter, arc)

# ball pit problem (3)
def volume_of_pit(pit_radius, pit_height):
  global pit_volume
  pit_volume = 3.14 * (pit_radius ** 2) * pit_height
  

pit_radius = float(input("Enter radius of pit: "))
pit_height = float(input("Enter height of pit: "))
volume_of_pit(pit_radius, pit_height)


def volume_of_ball(ball_radius):
  global ball_volume
  ball_volume = (4/3) * 3.14 * (ball_radius ** 3)
  

ball_radius = float(input("Enter radius of one ball: "))
volume_of_ball(ball_radius)

packing_density = 0.75

number_of_balls = pit_volume / ball_volume * packing_density
print("You need", number_of_balls, "balls")

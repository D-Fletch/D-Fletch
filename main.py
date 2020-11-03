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

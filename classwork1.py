№ 1
n = int(input())
a = int(input())
c = int(input())
sum = n + a + c
umn = n * a * c
sr = (n + a + c)/3
print("Сумма чисел:", sum)
print("Произведение чисел:", umn)
print("Среднее арифметическое чисел:", sr)


№2
from math import * 
xa = int (input ('xa= ')) 
ya = int (input ('ya= ')) 
xb = int (input ('xb= ')) 
yb = int (input ('yb= ')) 
d = sqrt ((xb - xa)**2 + (yb - ya)**2) 
print ('|AB| =', d)


№3
a = int(input())
b = int(input())
if a == b:
	print('True')


№4
def ipis(a,b):
      if abs(a)<=1 and abs(b)<=1:
            return True
      else:
            return False
 def IsPointInSquare(a,b):
      return ipis(a,b)



№5
print("Введите координату x:")
x = float(input())
print("Введите координату y:")
y = float(input())
print("Введите радиус круга:")
n = int(input())

dl = (x**2 + y**2)**(1/2)
if dl <= n :
    print("Точка попадает в круг")
else:
    print("Точка лежит за пределами круга")



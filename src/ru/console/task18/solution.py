import console
a = console.get_value("a")
b = console.get_value("b")

if a > 5 and a % 2 == 0:
  console.set_value("c", a / 2)
elif a <= 5 or a == b:
  console.set_value("c", b)
else: 
  console.set_value("c", 0)

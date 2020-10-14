import console
a = console.get_value("a")
b = console.get_value("b")

if a * 2 > b:
  console.set_value("c", a + b)
  c = console.get_value("c")
  if c > 10:
    console.set_value("d", c / 2)
  elif c > 5:
    console.set_value("d", c * 2)
  else:
    console.set_value("d", 5)
elif a * 2 ==  b:
  console.set_value("d", a ** 2)
else: 
  console.set_value("d", b ** 3)

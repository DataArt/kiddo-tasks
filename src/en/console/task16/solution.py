import console
a = console.get_value("a")
b = console.get_value("b")
if a == 2:
  console.set_value("c",  a + b)
elif a == 1:
  console.set_value("c",  b - a)
elif a == 0:
  console.set_value("c",  0)

import console
a = console.get_value("a")
b = console.get_value("b")
if b != 0:
  console.set_value("c",  a / b)
else:
  console.set_value("c",  a)

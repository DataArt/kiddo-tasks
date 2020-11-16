import console
a = console.get_value("a")
b = console.get_value("b")
if a <= b:
  console.set_value("c",  a * 2)
else:
  console.set_value("c",  b * 2)

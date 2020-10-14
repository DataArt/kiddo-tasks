import console
a = console.get_value("a")
b = console.get_value("b")
if a > b:
  console.set_value("c",  a % b)
  c = console.get_value("c")
  if c > 0.5:
    console.set_value("c",  c * 2)
else:
  console.set_value("c",  b % a)

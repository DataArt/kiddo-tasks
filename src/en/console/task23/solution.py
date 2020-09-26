import console
n = console.get_value("n")
c = 0

for i in range(n):
  if i % 2 == 0:
    c += 3
  else:
    c *= 2

console.set_value("c", c)
print(c)
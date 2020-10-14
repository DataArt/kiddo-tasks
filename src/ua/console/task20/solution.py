import console
n = console.get_value("n")
sum = 0
while n > 1:
  sum += 5
  n -= 2
console.set_value("z", sum)
print console.get_value("z")

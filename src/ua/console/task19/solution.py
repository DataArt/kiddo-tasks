import console
x = console.get_value("x")
y = console.get_value("y")
n = console.get_value("n")

sum = 0
for i in range(n):
    sum += (x + y) * 2

console.set_value("z", sum)
print console.get_value("z")

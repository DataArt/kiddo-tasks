import console

# # fail attempt to override readonly variable
# console.set_value("STR", "dog")

# # fail attempt to set value to nonexistent variable
# console.set_value("nonexistent_var", 10)

# # successful attempt to set variable value
# res = console.set_value("x", 24)

# # print values to console
# value_from_set = console.get_value("set")
# print value_from_set
# print console.get_value("RANGE")

# # put "RANGE" and "x" variable values to variable "result"
# value_from_range = console.get_value("RANGE")
# x = console.get_value("x")
# console.set_value("result", value_from_range + x)
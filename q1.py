variable = str(input("\n"))
print(len(variable))
print(variable[::-1])
x = slice(10,27)
print(variable[x])
replacement = variable.replace("a case sensitive","object oriented")
print(replacement)
result = variable.index('a')
print(result)
space = " "
y = ""
for char in variable:
    if char != space:
        y = y + char
print(y)



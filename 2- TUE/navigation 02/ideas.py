max = 10

result = ""
for i in range(1, max):
    for j in range(1, max):
        result += str(i) + "X" + str(j) + "=" + str(i*j) + "\n"
    result += "_________________________" + "\n"

print(result)
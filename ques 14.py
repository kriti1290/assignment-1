
lines = []

while True:
    line = input("Enter a line (empty line to stop): ")
    if line == "":
        break
    lines.append(line)

print("Lines entered:")
for line in lines:
    print(line)

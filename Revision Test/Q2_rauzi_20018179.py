#slightly different approach than suggested but I opted for simplicitiy

for i in range(10):
    output = ""
    for j in range(10-i):
        output += f"{j} "
    print(f"{output:>20}") 
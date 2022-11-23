inverso = []
for i in range(1, 6):
    print("*"*i)
for i in range(1, 5):
    inverso.append("*"*i)
inverso.reverse()
for i in inverso:
    print(i)

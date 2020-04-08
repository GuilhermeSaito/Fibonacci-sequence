t0 = 0
t1 = 1

n = int(input("How many do you want?: "))

print(t0)
print(t1)

cont = 3

while cont<=n:
    t2 = t0 + t1

    t0 = t1
    t1 = t2

    print(t2)
    cont += 1

# Fibonacci-sequence

t0 = 0
t1 = 1

n = int(input("Qunatos Números Você Quer?"))

print("{} - {}".format(t0, t1), end="")

cont = 3

while cont<=n:
    t2 = t0 + t1
    
    t0 = t1
    t1 = t2
    
    print(" - {}".format(t2), end="")
    cont += 1

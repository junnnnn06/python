cut = 1
while cut <= 100:
    if cut%3 == 0:
        print("fizz")
    elif cut%5 == 0:
        print("buzz")
    elif cut%3 == 0 and cut%5 == 0:
        print("fizzbuzz")
    else:
        print(cut)
    cut += 1

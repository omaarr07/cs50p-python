while True:
    try:
        x=int(input("What is the value of x"))
    except ValueError:
        print("X is not an integer")
    else:
        break
print(f"x is {x}")
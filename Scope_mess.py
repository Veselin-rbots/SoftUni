x = "global"

def outer():
    x = "Local"

    def inner():
        nonlocal  x
        x = "nonLocal"
        print("ïnner", x)

    def change.global():
        global x
        x = "global: Changed"

    print("outer:", x)
    inner()
    print("outer:", x)
    change.global()

print(x)
outer()
print(x)

def getAB(num):
    a, b = "", ""
    i = 0
    while i < len(num):
        if num[i] == ".":
            b += num[i+1:]
            break
        a += num[i]
        i += 1

    return (a,b)


def add_str(num1, num2):
    a1, a2 = getAB(num1)
    b1, b2 = getAB(num2)


    la, lb = len(a2), len(b2)
    if la > lb:
        b2 += "0"*(la-lb)
    elif lb > la:
        a2 += "0"*(lb-la)

    a = float(a1 + "." + a2)
    b = float(b1 + "." + b2)
    return a+b

print(add_str("11.11", "22.22"))
print(add_str("11.11", "77.778"))
print(add_str("0.0", ".888"))
print(add_str("123.52", "11.2"))
print(add_str("110.75", "9"))
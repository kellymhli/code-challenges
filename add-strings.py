def add_str(num1, num2):
    n1 = num1.split(".")
    n2 = num2.split(".")
    for i, n in enumerate(n1):
        if n == "":
            n1[i] = 0
    for i, n in enumerate(n2):
        if n == "":
            n2[i] = 0

    l1, l2 = len(n1[-1]), len(n2[-1])
    if l1 > l2:
        n2[-1] += "0"*(l1-l2)
    elif l2 > l1:
        n1[-1] += "0"*(l2-l1)

    a = str(int(n1[0]) + int(n2[0]))
    b = str(int(n1[1]) + int(n2[1]))
    res = a + "." + b
    return float(res)

print(add_str("11.11", "22.22"))
print(add_str("11.11", "77.778"))
print(add_str("0.0", ".888"))
def to_4(x):
    s = ""
    while x > 0:
        t = x % 4
        s = str(t) + s
        x = x // 4
    return s
print(to_4(98))

def to_3(x):
    s = ""
    while x > 0:
        t = x % 3
        s = str(t) + s
        x = x // 3
    return s
print(to_3(2307))

print(f"{675:o}")
print(f"{7000:x}")



def two_one_counter(x):
    s = 0
    while x > 0:
        t = x % 2
        if t == 1:
            s+=1
        x = x // 2
    return s
print(two_one_counter(195))
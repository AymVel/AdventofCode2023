
def search(temp,digit):
    b = None
    for l in digit:
        if temp.find(l) != -1:
            index = digit.index(l)
            b = str(index + 1)
            break
    return b

res = []
digit = ["one","two","three","four","five","six","seven","eight","nine","ten"]

for s in [*open("day1/day1")]:
    temp = ""
    a = None
    b = None
    for i in s:
        temp = temp+i
        if i.isdigit():
            a = i
            break
        t = search(temp,digit)
        if t != None:
            a = t
            break

    temp2 = ""
    for i in reversed(s[:len(s)-1]):
        temp2 = i+temp2
        t = search(temp2, digit)
        if t != None:
            b = t
            break
        if i.isdigit():
            b = i
            break

    if a != None:
        if b!= None:
            res.append(int(a+b))

        else:
            res.append(int(a+a))

    else:
        res.append(int(b+b))


print(sum(res))


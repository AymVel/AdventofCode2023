import re

green = 13
blue = 14
red = 12
total = 0
colors = ["green" ,"blue", "red"]
for s in [*open("day2")]:
    temp_green = 0
    temp_red = 0
    temp_blue = 0
    for c in colors:
        res = [m.start() for m in re.finditer(c, s)]
        for i in res:

            if c == "green":
                if int(s[i-3] + s[i-2]) > temp_green:
                    temp_green = int(s[i-3] +s[i-2])
            if c == "blue":
                if int(s[i-3] + s[i - 2]) > temp_blue:
                    temp_blue = int(s[i-3] +s[i - 2])
            if c == "red":
                if int(s[i-3] + s[i - 2]) > temp_red:
                    temp_red = int(s[i-3] + s[i - 2])

    total+=(temp_green*temp_red*temp_blue)
print(total)

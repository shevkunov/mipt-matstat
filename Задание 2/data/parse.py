file = open("weather.csv", "r")
out = open("py-weather.txt", "w")
s = "["
for line in file:
    for c in line:
        if c in "0123456789":
            s += c
    s += ","
s += "]";
out.write(s)
out.close()    

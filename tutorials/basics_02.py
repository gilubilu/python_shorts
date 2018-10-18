# string alignment and padding strings

print("{}, {}!".format("hello", "world"))
print("{0}{1}{0}".format("abra","cad"))
print("{first} {last}".format(first="Gilbert", last="Micallef"))

print("{a:<10}|{a:^10}|{a:>10}".format(a="test"))
print("{a:-<10}|{a:-^10}|{a:->10}".format(a="test"))

person = {"first":"Gilbert", "last":"Micallef"}
print("{p[first]} {p[last]}".format(p=person))

date = range(100)
print("{d[0]}...{d[99]}".format(d=date))

print("normal int:{num:d}".format(num=33))
print("normal float:{num:f}".format(num=33))
print("binary:{num:b}".format(num=33))
print("padded binary:{num:08b}".format(num=33))
print("hex:{num:x}".format(num=33))
print("paddedd hex:0x{num:0<4x}".format(num=33))
print("octal:{num:o}".format(num=33))

print("{num:f}".format(num=22/7))
print("{num:0.2f}".format(num=22/7))
print("{num:0.2e}".format(num=22/7))
print("{num:0.2%}".format(num=22/7))

print("{num:g}".format(num=5.0000001)) # not recommended
print("{num:g}".format(num=5.1200001))

var=27
print(f"{var}")


s = input()
i = ord(s)

if i == ord("a"):
    i = ord("z")
else:
    i -= 1
print(chr(i))
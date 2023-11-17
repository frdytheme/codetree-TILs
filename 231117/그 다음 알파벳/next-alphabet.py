s = input()

i = ord(s)
if i == ord("z"):
    i = ord("a")
else:
    i = i + 1
print(chr(i))
info = input().split()
h, w = int(info[0]), int(info[1])
h = (h / 100) ** 2
bmi = int(w/h)
if bmi >= 25:
    print(f"{bmi}\nObesity")
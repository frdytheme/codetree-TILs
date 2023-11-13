y = int(input())

if y % 4 == 0:
    if(y % 100 == 0):
        if(y % 400 == 0):
            print("true")
        print("false")
    print("true")
else:
    print("false")
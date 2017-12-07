def star(num):
    if num < 10:
        star(num + 1)
    print("*" * num)


star(1)
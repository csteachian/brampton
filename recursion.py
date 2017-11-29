
def stars(output):
    if len(output) < 990:
        print(output)
        output = stars(output+"*")
    else:
        print(output)
    return output

stars("*")
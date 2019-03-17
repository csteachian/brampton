# Recursion example
# Ian Simpson @familysimpson

# Inspired by https://www.youtube.com/watch?v=gogV1vUVKH8

def recur(n):
    print("N =",n)
    if n <= 10:
        print("N <= 10: RETURN",n*2)
        return n * 2
    else:
        print("N > 10: RETURN CALL RECUR(CALL RECUR(",n/3,")")
        return recur(recur(n/3))

#main program
print("Recursion example 2")
print("CALL recur(27)")
print(int(recur(27))) # convert returned value from float to integer before display
